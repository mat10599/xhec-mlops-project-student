# Use this module to code a `pickle_object` function. This will be useful to pickle the model (and encoder if need be).
import pickle
import os
import pandas as pd

NUMERICAL_COLS = [
    "Length",
    "Diameter",
    "Height",
    "Whole weight",
    "Shucked weight",
    "Viscera weight",
    "Shell weight",
]

ROOT_PATH = os.getcwd()
LOCAL_OBJECTS_PATH = os.path.join(ROOT_PATH, "src/web_service/local_objects")
MODEL_PATH = os.path.join(LOCAL_OBJECTS_PATH, "model.pkl")
DATA_PATH = os.path.join(ROOT_PATH, "data/abalone.csv")


def read_data(dataset_path: str) -> pd.DataFrame:
    """Read the data at the given path and return a dataframe."""
    df = pd.read_csv(dataset_path)
    return df


def save_pickle(obj, path: str):
    """save pickle object

    Args:
        obj (_type_): object to pickle
        path (_type_): path of the pickle file
    """
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(path: str):
    """load pickle object

    Args:
        obj (_type_): object to load
    """
    with open(path, "rb") as f:
        return pickle.load(f)
