import os
from typing import Optional

import numpy as np
from utils import read_data, load_pickle, save_pickle
from loguru import logger

# from modeling import evaluate_model, predict, train_model
from prefect import flow
from preprocessing import preprocessing
from training import train_model
from predicting import predict
from config import DATA_PATH
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBRegressor


@flow(name="Train model")
def train_model_workflow(
    train_filepath: str,
    artifacts_filepath: Optional[str] = None,
) -> dict:
    """Train a model and save it to a file"""
    logger.info("Read data from local files...")
    data = read_data(dataset_path=train_filepath)
    logger.info("Processing training data...")
    processed_data, numerical_encoders, label_encoder = preprocessing(data, training=True)
    logger.info("Training model...")
    model = train_model(processed_data)

    if artifacts_filepath is not None:
        logger.info(f"Saving artifacts to {artifacts_filepath}...")
        save_pickle(model, os.path.join(artifacts_filepath, "model.pkl"))
        save_pickle(numerical_encoders, os.path.join(artifacts_filepath, "numerical_encoders.pkl"))
        save_pickle(label_encoder, os.path.join(artifacts_filepath, "label_encoder.pkl"))

    return {"model": model, "numerical_endoers": numerical_encoders, "label_encoder": label_encoder}


@flow(name="Batch predict", retries=1, retry_delay_seconds=30)
def batch_predict_workflow(
    input_filepath: str,
    model: Optional[XGBRegressor] = None,
    numerical_encoders: Optional[StandardScaler] = None,
    label_encoder: Optional[LabelEncoder] = None,
    artifacts_filepath: Optional[str] = None,
) -> np.ndarray:
    """Make predictions on a new dataset"""
    logger.info("Retrieving models...")
    if numerical_encoders is None:
        numerical_encoders = load_pickle(os.path.join(artifacts_filepath, "numerical_encoders.pkl"))
    if label_encoder is None:
        label_encoder = load_pickle(os.path.join(artifacts_filepath, "label_encoder.pkl"))
    if model is None:
        model = load_pickle(os.path.join(artifacts_filepath, "model.pkl"))

    logger.info("Preprocessing data...")
    X, _, _ = preprocessing(
        filepath=input_filepath,
        training=False,
        scaler=numerical_encoders,
        label_encoder=label_encoder,
    )
    logger.info("Predicting data...")
    y_pred = predict(model=model, input_data=X)

    return y_pred


if __name__ == "__main__":
    from config import DATA_PATH, LOCAL_OBJECTS_PATH

    train_model_workflow(
        train_filepath=DATA_PATH,
        artifacts_filepath=LOCAL_OBJECTS_PATH,
    )

    batch_predict_workflow(
        input_filepath=DATA_PATH,
        artifacts_filepath=MODELS_DIRPATH,
    )
