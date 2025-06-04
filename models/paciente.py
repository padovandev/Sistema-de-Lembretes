from dataclasses import dataclass

@dataclass
class Paciente:
    id: int
    nome: str
    cpf: int 
    telefone: str
    email: str
    dn: str

