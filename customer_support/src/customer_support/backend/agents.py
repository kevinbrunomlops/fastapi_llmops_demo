from pydantic_ai import Agent
from sre_constants import MODEL_MEDIUM
from dotenv import load_dotenv

load_dotenv()

suppoert_agent = Agent(
    model=MODEL_MEDIUM, system_prompt="You are a customer support agent"
)

