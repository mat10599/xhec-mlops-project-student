import os

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from utils import save_pickle
from config import LOCAL_OBJECTS_PATH, NUMERICAL_COLS


def preprocessing(
        df: pd.DataFrame,
        training: bool = False,
        scaler:StandardScaler = None,
        label_encoder: LabelEncoder = None) -> pd.DataFrame:

    if training:
        df['age'] = df['Rings']+1.5
        df = df.drop('Rings', axis=1)
        label_encoder = LabelEncoder()
        numerical_encoders = StandardScaler()
        df[NUMERICAL_COLS] = numerical_encoders.fit_transform(df[NUMERICAL_COLS])
        df["Sex"] = label_encoder.fit_transform(df["Sex"])
        save_pickle(numerical_encoders, os.path.join(LOCAL_OBJECTS_PATH, "numerical_encoders.pkl"))
        save_pickle(label_encoder, os.path.join(LOCAL_OBJECTS_PATH, "label_encoder.pkl"))
    else:
        df[[NUMERICAL_COLS]] = scaler.transform(df[[NUMERICAL_COLS]])
        df["Sex"] = label_encoder.transform(df["Sex"])

    return df
