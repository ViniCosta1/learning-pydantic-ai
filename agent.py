from pydantic_ai import Agent, Tool

from tools import *
from models import *

system_prompt = """\
Você é um assistente que ajuda usuários a encontrar informações sobre CEPs no Brasil.
Você deve buscar informações do CEP fornecido pelo usuário e retornar o nome do usuário junto com as informações do CEP.
Retorne apenas o nome do usuário e as informações do CEP, sem explicações adicionais.
"""

agent = Agent(
    'google-gla:gemini-1.5-flash',
    deps_type=UserCepModel,
    output_type=[CepReturnModel],
    tools=[
        Tool(get_cep_info)
    ],
    system_prompt=system_prompt,
)

@agent.system_prompt
async def add_user_name(ctx: RunContext[UserCepModel]) -> str:
    """Retorno do nome do usuário"""

    return ctx.deps.nome