from typing import List, Tuple

import pandas as pd
from config import NUMERICAL_COLS
from sklearn.preprocessing import LabelEncoder, StandardScaler
from utils import save_pickle
from config import LOCAL_OBJECTS_PATH, NUMERICAL_COLS
from prefect import flow, task


@flow(name="Preprocess data")
def preprocessing(
    df: pd.DataFrame,
    training: bool = True,
    scaler: StandardScaler = None,
    label_encoder: LabelEncoder = None,
) -> Tuple[pd.DataFrame, StandardScaler, LabelEncoder]:
    """Preprocess the data, apply standard scaler and label encoder if
    training is True, else apply the same transformations as in training.

    Args:
        df (pd.DataFrame): raw data to be preprocessed
        training (bool, optional): state whether we are preprocessing training
        data or predicting data . Defaults to True.
        scaler (StandardScaler, optional): if predicting data, provide the
        scaler object. Defaults to None.
        label_encoder (LabelEncoder, optional): if predicting data, provide
        the label_encoder object. Defaults to None.

    Returns:
        pd.DataFrame: preprocessed df

    Raises:
        ValueError: if scaler or label_encoder are not provided in predicting
        mode
    """
    if not training:
        # check if scaler and label_encoder are provided
        if scaler is None or label_encoder is None:
            raise ValueError("Please provide scaler and label_encoder objects in predicting mode")
    if training:
        df["age"] = df["Rings"] + 1.5
        df = df.drop("Rings", axis=1)

        label_encoder = LabelEncoder()
        numerical_encoders = StandardScaler()
        df[NUMERICAL_COLS] = numerical_encoders.fit_transform(df[NUMERICAL_COLS])
        df["Sex"] = label_encoder.fit_transform(df["Sex"])

        return df, numerical_encoders, label_encoder

    else:
        df[NUMERICAL_COLS] = scaler.transform(df[NUMERICAL_COLS])
        df["Sex"] = label_encoder.transform(df["Sex"])

    return df, None, None
