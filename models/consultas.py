from dataclasses import dataclass
from utils.db import connect_db

@dataclass
class Consultas:
    id: int
    consulta_id: int
    data: str # formato ISO: 'YYYY-MM-DD HH:MM'
    observacoes: str

def buscar_consultas(inicio, fim):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.id, p.nome, c.data, c.observacoes
        FROM consultas c
        JOIN pacientes p ON c.paciente_id = p.id
        WHERE datetime(c.data) BETWEEN ? AND ?
    """, (inicio.isoformat(), fim.isoformat()))
    consultas = cursor.fetchall()
    conn.close()
    return consultas