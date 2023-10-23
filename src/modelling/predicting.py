import pandas as pd
from preprocessing import preprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBRegressor
from prefect import flow, task


@task(name="Predict model")
def predict(
    model: XGBRegressor,
    input_data: pd.DataFrame,
    scaler: StandardScaler,
    label_encoder: LabelEncoder,
):
    preprocessed_data = preprocessing(
        input_data, training=False, scaler=scaler, label_encoder=label_encoder
    )
    predictions = model.predict(preprocessed_data)

    return predictions
