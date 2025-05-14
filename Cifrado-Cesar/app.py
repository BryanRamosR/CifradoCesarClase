from flask import Flask, render_template, request
from datetime import datetime
import sqlite3
import os
import Encryptor
import Db

app = Flask(__name__)
DB_PATH = 'database.db'

@app.route("/", methods=["GET", "POST"])
def inicio():
    encrypted = ""
    text = ""
    shift = 0

    if request.method == "POST":
        text = request.form.get('text', '')
        shift = int(request.form.get('shift', 0))
        encryptor = Encryptor.Encryptor(shift)
        encrypted = encryptor.encrypt(text)

        # Guardar en la base de datos
        Db.save_encrypted_text(DB_PATH, shift, text, encrypted)

    # Cargar historial
    historial = Db.get_historial(DB_PATH)

    return render_template("index.html", text=text, shift=shift, encrypted=encrypted, historial=historial)

if __name__ == "__main__":
    Db.init_db(DB_PATH)
    app.run(debug=True)
