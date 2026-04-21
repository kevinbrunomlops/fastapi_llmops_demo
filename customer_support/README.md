# 📦 Customer Support Bot (FastAPI + Streamlit + MLflow)
This project demonstrates a simple LLM-powered customer support bot using:

FastAPI → backend API
Streamlit → frontend UI
MLflow → logging, tracing, and evaluation
PydanticAI → agent + tooling

## 🧠 Functionality
- An LLM agent answers customer questions
- A tool (lookup_faq) is used to look up FAQ
- API exposes endpoint /customer_support
- Streamlit UI calls the API
- MLflow logs:
    - latency
    - status codes
    - parameters

´´´
customer_support/
│
├── src/customer_support/
│   ├── backend/
│   │   ├── agents.py          # LLM-agent + tools
│   │   ├── api.py             # FastAPI endpoints
│   │   ├── constants.py       # Modellval + MLflow config
│   │   └── middlewares.py     # MLflow logging middleware
│   │
│   ├── frontend/
│   │   └── app.py             # Streamlit UI
│   │
│   ├── monitoring/
│   │   ├── eval_data.json     # Eval dataset
│   │   ├── mlflow.db          # MLflow SQLite DB
│   │   ├── monitoring.ipynb   # Analys
│   │   └── prompts.ipynb      # Prompt engineering
│   │
│   └── __init__.py
│
├── .env
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
´´´