from fastapi import FastAPI
from customer_support.backend.agents import support_agent

app = FastAPI()

# get for simplicity -> in real cases use post
@app.get("/customer_support")
async def customer_support_faq(question: str) -> str:
    result = await support_agent.run(question)
    return result.output