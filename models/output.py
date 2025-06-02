from pydantic import BaseModel

class CepReturnModel(BaseModel):
    """Modelo de retorno do CEP"""
    
    nome: str
    cep: str
    logradouro: str
    bairro: str
    localidade: str
    uf: str