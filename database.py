import sqlite3
import datetime

DB_PATH = "real_estate.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create History Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            overall_qual INTEGER,
            gr_liv_area INTEGER,
            garage_cars INTEGER,
            garage_area INTEGER,
            total_bsmt_sf INTEGER,
            full_bath INTEGER,
            year_built INTEGER,
            predicted_price REAL,
            timestamp TEXT
        )
    ''')
    
    # Create Favorites Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            overall_qual INTEGER,
            gr_liv_area INTEGER,
            garage_cars INTEGER,
            garage_area INTEGER,
            total_bsmt_sf INTEGER,
            full_bath INTEGER,
            year_built INTEGER,
            predicted_price REAL,
            notes TEXT,
            timestamp TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def add_to_history(features, predicted_price):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO history (overall_qual, gr_liv_area, garage_cars, garage_area, 
                            total_bsmt_sf, full_bath, year_built, predicted_price, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (features['OverallQual'], features['GrLivArea'], features['GarageCars'], 
          features['GarageArea'], features['TotalBsmtSF'], features['FullBath'], 
          features['YearBuilt'], predicted_price, timestamp))
    
    conn.commit()
    history_id = cursor.lastrowid
    conn.close()
    return history_id

def get_history():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_prediction_by_id(record_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history WHERE id = ?', (record_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None

def add_favorite(record_id, notes=""):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get from history
    cursor.execute('SELECT * FROM history WHERE id = ?', (record_id,))
    row = cursor.fetchone()
    
    if row:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO favorites (overall_qual, gr_liv_area, garage_cars, garage_area, 
                                total_bsmt_sf, full_bath, year_built, predicted_price, notes, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['overall_qual'], row['gr_liv_area'], row['garage_cars'], 
              row['garage_area'], row['total_bsmt_sf'], row['full_bath'], 
              row['year_built'], row['predicted_price'], notes, timestamp))
        conn.commit()
    conn.close()

def get_favorites():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM favorites ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def remove_favorite(favorite_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM favorites WHERE id = ?', (favorite_id,))
    conn.commit()
    conn.close()
    
def remove_history(history_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM history WHERE id = ?', (history_id,))
    conn.commit()
    conn.close()
