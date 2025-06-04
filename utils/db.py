import sqlite3
import os 

def connect_db():
    db_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'database.db')
    return sqlite3.connect("data/database.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf INTEGER, 
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT,
            dn TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER,
            data TEXT NOT NULL,
            observacoes TEXT,
            FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lembretes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            consulta_id INTEGER,
            enviado INTEGER DEFAULT 0,
            data_envio TEXT,
            FOREIGN KEY(id) REFERENCES consultas(id)
        );
    """)

    conn.commit()
    conn.close()