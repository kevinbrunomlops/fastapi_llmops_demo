from pathlib import Path
import mlflow


MODEL_SMALL="openrouter:liquid/lfm-2.5-1.2b-instruct:free"
MODEL_MEDIUM="openrouter:nvidia/nemotron-3-nano-30b-a3b:free"
MODEL_LARGE="openrouter:nvidia/nemotron-3-super-120b-a12b:free"

LLM_JUDGE="openrouter:/nvidia/nemotron-3-nano-30b-a3b:free"

MONITORING_PATH = Path(__file__).parents[1] / "monitoring"

# when constants module is imported -> this will run -> we use mlflow.db inside of monitoring
mlflow.set_tracking_uri(f"sqlite:///{MONITORING_PATH / 'mlflow.db'}")
mlflow.set_experiment("customer_support_bot")
mlflow.pydantic_ai.autolog()