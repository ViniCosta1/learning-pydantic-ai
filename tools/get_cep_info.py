from pydantic_ai import RunContext
from models import UserCepModel

import os
import requests

def get_cep_info(ctx: RunContext[UserCepModel]) -> dict:
    """Busca informações do CEP do usuário"""

    cep = ctx.deps.cep

    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, f"data/cep_info_{cep}.json")
    print(current_dir)

    # Buscando informações do CEP
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    with open(file_path, "w") as file:
        file.write(response.text)

    return response.json()