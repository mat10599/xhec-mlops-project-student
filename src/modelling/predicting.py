import pandas as pd
import pickle
from xgboost import XGBRegressor
from preprocessing import preprocessing
from sklearn.preprocessing import StandardScaler, LabelEncoder


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
