# 🏠 EstiMate | Premium House Price Predictor Web App

## 📌 Overview

This project is a modern, premium, production-ready web application for predicting house sale prices using Machine Learning techniques on the Ames Housing Dataset.

It has been completely upgraded from a basic Jupyter Notebook into a full-stack Flask application with a beautiful, responsive UI using Tailwind CSS and interactive charts using Chart.js.

---

## 🌟 Key Features

1. **Interactive Dashboard**: View market statistics, recent predictions, and price trends.
2. **AI-Powered Valuation**: Enter property details to get an instant, machine-learning-backed price estimate.
3. **Valuation Reports**: Detailed result pages breaking down the value contribution of different property features.
4. **Prediction History**: Automatically saves your past predictions in a local SQLite database for easy access.
5. **Favorites**: Shortlist and save your most important valuations.
6. **Property Comparison**: Compare up to 3 different properties side-by-side.
7. **Market Insights**: Visual charts showing price distribution by quality and age.

---

## 🛠️ Technology Stack

- **Backend**: Python, Flask, SQLite
- **Machine Learning**: Pandas, Scikit-Learn (Random Forest Regressor)
- **Frontend**: HTML5, Tailwind CSS, Chart.js, Phosphor Icons
- **Architecture**: Modular design separating UI (`templates/`), database (`database.py`), ML model (`model.py`), and routing (`app.py`).

---

## 🚀 Quick Start

1. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Access the Web App**:
   Open your browser and navigate to `http://localhost:5000`

*Note: If `train.csv` is not present in the directory, the application will automatically attempt to fetch the dataset from OpenML, or fallback to a dummy model to ensure the UI remains fully functional.*

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── app.py                 # Main Flask application and routing
├── model.py               # Machine Learning model training and inference
├── database.py            # SQLite database for History & Favorites
├── requirements.txt       # Python dependencies
├── houseprice.ipynb       # Original exploratory data analysis notebook
├── README.md              # Project documentation
│
├── templates/             # HTML Templates
│   ├── base.html          # Base layout with sidebar and navigation
│   ├── index.html         # Dashboard
│   ├── predict.html       # Prediction input form
│   ├── result.html        # Detailed valuation report
│   ├── history.html       # Prediction history
│   ├── favorites.html     # Saved properties
│   ├── comparison.html    # Side-by-side comparison
│   └── insights.html      # Market analytics charts
│
└── static/                # Static assets (CSS/JS - linked via CDN in this build)
```

---

## 👨‍💻 Author

**Prabhash Verma**
M.Tech Data Science Student

(Upgraded to a full-stack premium application as requested)
