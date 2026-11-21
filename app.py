from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os
import model
import database

app = Flask(__name__)
app.secret_key = 'super_secret_premium_key'

# Initialize database
database.init_db()

# Pre-train or load model on startup
try:
    model.load_or_train_model()
except Exception as e:
    print(f"Startup model check error: {e}")

@app.route('/auth')
def auth():
    return render_template('auth.html', hide_sidebar=True)

@app.route('/')
def dashboard():
    stats = model.get_market_stats()
    recent_history = database.get_history()[:5]
    return render_template('index.html', stats=stats, recent_history=recent_history, active_page='dashboard')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            features = {
                'OverallQual': int(request.form.get('overall_qual')),
                'GrLivArea': int(request.form.get('gr_liv_area')),
                'GarageCars': int(request.form.get('garage_cars')),
                'GarageArea': int(request.form.get('garage_area')),
                'TotalBsmtSF': int(request.form.get('total_bsmt_sf')),
                'FullBath': int(request.form.get('full_bath')),
                'YearBuilt': int(request.form.get('year_built'))
            }
            
            prediction = model.predict_price(features)
            
            # Save to history
            record_id = database.add_to_history(features, prediction)
            
            return redirect(url_for('result', record_id=record_id))
            
        except Exception as e:
            flash(f'Error processing prediction: {str(e)}', 'error')
            
    return render_template('predict.html', active_page='predict')

@app.route('/result/<int:record_id>')
def result(record_id):
    record = database.get_prediction_by_id(record_id)
    if not record:
        flash('Prediction record not found.', 'error')
        return redirect(url_for('history'))
        
    return render_template('result.html', record=record, active_page='predict')

@app.route('/history')
def history():
    records = database.get_history()
    return render_template('history.html', records=records, active_page='history')

@app.route('/history/delete/<int:record_id>', methods=['POST'])
def delete_history(record_id):
    database.remove_history(record_id)
    flash('Record deleted successfully.', 'success')
    return redirect(url_for('history'))

@app.route('/favorites')
def favorites():
    records = database.get_favorites()
    return render_template('favorites.html', records=records, active_page='favorites')

@app.route('/favorites/add/<int:record_id>', methods=['POST'])
def add_favorite(record_id):
    database.add_favorite(record_id)
    flash('Added to favorites.', 'success')
    return redirect(url_for('result', record_id=record_id))

@app.route('/favorites/remove/<int:record_id>', methods=['POST'])
def remove_favorite(record_id):
    database.remove_favorite(record_id)
    flash('Removed from favorites.', 'success')
    return redirect(url_for('favorites'))

@app.route('/comparison')
def comparison():
    records = database.get_history()
    return render_template('comparison.html', records=records, active_page='comparison')

@app.route('/insights')
def insights():
    stats = model.get_market_stats()
    return render_template('insights.html', stats=stats, active_page='insights')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
