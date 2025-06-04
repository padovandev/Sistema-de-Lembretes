import sqlite3
from utils.db import connect_db
from models.consultas import Consultas

def agendar_consulta(paciente_id, data, observacoes):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO consultas (paciente_id, data, observacoes)
    VALUES (?, ?, ?)
    """, (paciente_id, data, observacoes))

    conn.commit()
    conn.close()

    print("Consulta Agendada com Sucesso...")

def listar_consultas():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT consultas.id, pacientes.nome, consultas.data, consultas.observacoes
        FROM consultas
        INNER JOIN pacientes ON consultas.paciente_id = pacientes.id
        ORDER BY consultas.data ASC;
    """)

    resultados = cursor.fetchall()
    conn.close()
    return resultados

def cancelar_consulta(consulta_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Remove lembretes associados
    cursor.execute("DELETE FROM lembretes WHERE consulta_id = ?", (consulta_id,))
    # Remove a consulta
    cursor.execute("DELETE FROM consultas WHERE id = ?", (consulta_id,))

    conn.commit()
    conn.close()
    print("Consulta cancelada com sucesso.")

def editar_consulta(consulta_id, nova_data, novas_observacoes):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE consultas
        SET data = ?, observacoes = ?
        WHERE id = ?;
    """, (nova_data, novas_observacoes, consulta_id))

    conn.commit()
    conn.close()
    print("Consulta editada com sucesso...")