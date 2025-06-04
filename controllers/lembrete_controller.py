from utils.db import connect_db
from models.lembrete import Lembrete
from models.consultas import Consultas
from datetime import datetime, timedelta

def enviar_lembretes():
    agora = datetime.now()
    daqui_24h = agora + timedelta(hours=24)

    consultas = Consultas.buscar_consultas(agora, daqui_24h)

    if not consultas:
        print("Nenhum lembrete a ser enviado.")
        return

    for c in consultas:
        print(f"Lembrete enviado para {c[1]} - Consulta em {c[2]}")  # Aqui você poderia enviar e-mail, SMS, etc.