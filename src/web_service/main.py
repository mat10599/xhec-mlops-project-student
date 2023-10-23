from app_config import (
    MODEL_PATH,
    PREPROCESSOR_PATH,
    LABEL_ENCODER_PATH, 
    APP_TITLE, 
    APP_DESCRIPTION
)


from fastapi import FastAPI
from lib.inference import run_inference
from lib.models import InputData, PredictionOut
from lib.utils import load_model, load_preprocessor, load_label_encoder

# Other imports

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION)


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionOut, status_code=201)
def predict(metrics: InputData) -> dict:
    pp = load_preprocessor(PREPROCESSOR_PATH)
    model = load_model(MODEL_PATH)
    label_encoder = load_label_encoder(LABEL_ENCODER_PATH)
    y = run_inference([metrics], pp, label_encoder, model)
    return {"Abalone age": y[0]}
