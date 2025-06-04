from dataclasses import dataclass

@dataclass
class Lembrete:
    id: int
    consulta_id: int
    enviado: bool
    data_envio: str  # formato ISO: 'YYYY-MM-DD HH:MM'