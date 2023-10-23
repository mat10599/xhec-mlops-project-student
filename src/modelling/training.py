import pandas as pd
import xgboost as xgb
from utils import save_pickle, MODEL_PATH


def extract_X_y(df: pd.DataFrame) -> None:
    """extract X and y from the dataframe

    Args:
        df (pd.DataFrame): preprocessed_df

    """
    X = df.drop("age", axis=1)
    y = df["age"]
    return X, y


def train_model(preprocessed_df: pd.DataFrame) -> None:
    """train xgboost model on preprocessed df and save it in pkl format

    Args:
        preprocessed_df (pd.DataFrame): preprocessed df
    """
    regressor = xgb.XGBRegressor()
    X, y = extract_X_y(preprocessed_df)
    regressor.fit(X, y)
    save_pickle(regressor, MODEL_PATH)
