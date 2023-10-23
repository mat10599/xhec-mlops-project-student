import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from prefect import flow, task


@task(name="Predict model")
def predict(input_data: pd.DataFrame, model: XGBRegressor) -> np.ndarray:
    predictions = model.predict(input_data)

    return predictions
