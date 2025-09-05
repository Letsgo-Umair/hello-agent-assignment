import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, OpenAIChatCompletionsModel

load_dotenv()  # Loads variables from .env

api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(external_client)
set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

agent = Agent(
    name="HelloAgent",
    instructions="You are a helpful assistant, specialized in providing single line response.",
    model=model
)

result = Runner.run_sync(agent, "Say hello in one short sentence.")

print(result.final_output)