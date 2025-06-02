from pydantic import BaseModel

class UserCepModel(BaseModel):
    """Modelo de CEP do usuário"""
    
    nome: str
    cep: str