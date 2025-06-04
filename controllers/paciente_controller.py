import sqlite3
from utils.db import connect_db
from models.paciente import Paciente

def cadastrar_paciente(nome, cpf, telefone, email, dn):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pacientes (nome, cpf, telefone, email, dn)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, cpf, telefone, email, dn))    

    conn.commit()
    cursor.close()
    print(f"O Paciente {nome} foi cadastrado com Sucesso. ")

def listar_pacientes():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pacientes")
    result = cursor.fetchall()

    conn.close()

    pacientes = []
    for row in result:
        paciente = Paciente(*row)
        pacientes.append(paciente)
    return pacientes

def buscar_nome(nome):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pacientes WHERE nome LIKE ?;", (f"%{nome}%",))
    result = cursor.fetchall()

    conn.close()

    pacientes = [Paciente(*row) for row in result]
    return pacientes