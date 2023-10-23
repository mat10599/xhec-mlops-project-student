from app_config import (
    MODEL_VERSION,
    PREPROCESSOR_FUNCT_NAME,
    MODEL_NAME,
    PATH_TO_PREPROCESSOR,
    PATH_TO_MODEL,
    CATEGORICAL_VARS,
    APP_TITLE, 
    APP_DESCRIPTION,
    APP_VERSION
)

from fastapi import FastAPI
from lib.modelling import run_inference
from lib.models import InputData, PredictionOut
from lib.utils import load_model, load_preprocessor

# Other imports

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION)


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model="InsertHereAPydanticClass", status_code=201)
def predict(payload: "InsertHereAPydanticClass") -> dict:
    # TODO: complete and replace the "InsertHereAPydanticClass" with the correct Pydantic classes defined in web_service/lib/models.py



from app_config import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    MODEL_VERSION,
    PATH_TO_MODEL,
    PATH_TO_PREPROCESSOR,
)
from fastapi import FastAPI

from lib.modelling import run_inference
from lib.models import InputData, PredictionOut
from lib.utils import load_model, load_preprocessor

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION)


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": MODEL_VERSION}


@app.post("/predict", response_model=PredictionOut, status_code=201)
def predict(payload: InputData):
    dv = load_preprocessor(PATH_TO_PREPROCESSOR)
    model = load_model(PATH_TO_MODEL)
    y = run_inference([payload], dv, model)
    return {"trip_duration_prediction": y[0]}
