from agent import *
from models import *

def run_agent():
    # Executa o agente e obtém o resultado
    deps = UserCepModel(
        nome='Vinícius',
        cep='16400629',
    )
    result = agent.run_sync('Consegue me trazer informações sobre o meu cep e salvá-las em um arquivo para que eu possa ter armazenado?', deps=deps)
    
    # Exibe informações sobre o resultado
    result.all_messages()

    print("Uso:", result.usage())
    print("Saída:", result.output)

if __name__ == "__main__":
    run_agent()