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

## Project structure
```
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
│   │   ├── mlflow.db          # MLflow DB
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
```

## ⚙️ Setup
1. Install dependencies

```uv sync```

## Running the application

1. Start the FastAPI backend

Go to the correct folder:

```cd src/customer_support/backend```

Start the server:

```uv run uvicorn api:app --reload```

API will be available at:

```http://127.0.0.1:8000```

Test endpoint:

```http://127.0.0.1:8000/docs```

2. Starta Streamlit frontend

open new terminal:

```cd src/customer_support/frontend```

Run:

```uv run streamlit run app.py```

Open in browser:

```http://localhost:8501```

## 📊 MLflow Monitoring

MLflow is automatically configured in constants.py:
- Tracking URI: local SQLite (mlflow.db)
- Experiment: customer_support_bot

Launch MLflow UI

``` uv run mlflow ui --port 5001```

Open:

```http://127.0.0.1:5001```

Here you can see:
- request latency
- errors
- endpoints
- runs per request

## 🧪 Evaluation

Eval data is located in:

``` monitoring/eval_data.json```

It contains:

- inputs (questions)

- expected_facts (what the model should say)

This is used for:
- LLM-as-a-judge
- quality control

## Architecture 
```
[User]
   ↓
[Streamlit UI]
   ↓ HTTP
[FastAPI API]
   ↓
[LLM Agent (PydanticAI)]
   ↓
[Tool: lookup_faq]
   ↓
[Response]
   ↓
[MLflow logging]
```