import sqlite3
import os
from datetime import datetime

def init_db(DB_PATH):
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE cifrados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                desplazamiento INTEGER,
                texto_original TEXT,
                texto_cifrado TEXT,
                fecha TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

def save_encrypted_text(DB_PATH, shift, text, encrypted_text):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cifrados (desplazamiento, texto_original, texto_cifrado, fecha)
        VALUES (?, ?, ?, ?)
    ''', (shift, text, encrypted_text, datetime.now()))
    conn.commit()
    conn.close()

def get_historial(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT desplazamiento, texto_original, texto_cifrado, fecha FROM cifrados ORDER BY id DESC')
    historial = cursor.fetchall()
    conn.close()
    return historial
