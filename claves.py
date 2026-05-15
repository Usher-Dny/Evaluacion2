import hashlib
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuración de base de datos SQL (Requerimiento)
def init_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS integrantes 
                      (nombre TEXT PRIMARY KEY, password_hash TEXT)''')
    conn.commit()
    conn.close()

# Hashing con sha256 (Requerimiento)
def generar_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def home():
    # Primera fase del contenido web (Requerimiento)
    return "<h1>Servidor de Credenciales Operativo - Puerto 5000</h1>"

@app.route('/verificar', methods=['POST'])
def verificar():
    # Leer parámetros de solicitud HTTP (Requerimiento)
    data = request.json
    user = data.get('nombre')
    passwd = data.get('password')
    # Aquí iría la lógica para verificar en la DB
    return jsonify({"usuario": user, "status": "recibido"})

if __name__ == '__main__':
    init_db()
    # El sitio web utilizará el puerto 5000 (Requerimiento)
    app.run(port=5000)
