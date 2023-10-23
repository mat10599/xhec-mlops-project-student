# Use this module to code a `pickle_object` function. This will be useful to pickle the model (and encoder if need be).
import pickle
import os
import pandas as pd


def read_data(dataset_path: str) -> pd.DataFrame:
    """Read the data at the given path and return a dataframe."""
    df = pd.read_csv(dataset_path)
    return df


def save_pickle(obj, path):
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)
