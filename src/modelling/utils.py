# Use this module to code a `pickle_object` function. This will be useful to
# pickle the model (and encoder if need be).
import pickle
from typing import Any
from prefect import flow, task

import pandas as pd


@task(name="Read data from path")
def read_data(dataset_path: str) -> pd.DataFrame:
    """Read the data at the given path and return a dataframe."""
    df = pd.read_csv(dataset_path)
    return df


@task(name="Save pickle")
def save_pickle(obj, path: str):
    """Save pickle object

    Args:
        obj (_type_): object to pickle
        path (_type_): path of the pickle file
    """
    with open(path, "wb") as f:
        pickle.dump(obj, f)


@task(name="Load pickle")
def load_pickle(path: str) -> Any:
    """Load pickle object

    Args:
        obj (_type_): object to load
    """
    with open(path, "rb") as f:
        return pickle.load(f)
