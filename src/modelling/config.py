import os

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
