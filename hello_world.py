from pydantic_ai import Agent

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    'google-gla:gemini-1.5-flash',
    system_prompt="Seja simples, responda com apenas uma frase!",
)

result = agent.run_sync('De onde a frase "Hello World!" vem?')
print(type(result))
print(result.output)
