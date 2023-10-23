from typing import List, Tuple

import pandas as pd
from xgboost import XGBRegressor
from prefect import flow, task


@task("Extract features and labels")
def extract_X_y(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Extract X and y from the dataframe

    Args:
        df (pd.DataFrame): preprocessed_df

    """
    X = df.drop("age", axis=1)
    y = df["age"]
    return X, y


@task(name="Train model")
def train_model(preprocessed_df: pd.DataFrame) -> XGBRegressor:
    """Train xgboost model on preprocessed df and save it in pkl format

    Args:
        preprocessed_df (pd.DataFrame): preprocessed df
    """
    regressor = XGBRegressor()
    X_train, y_train = extract_X_y(preprocessed_df)
    regressor.fit(X_train, y_train)

    return regressor
