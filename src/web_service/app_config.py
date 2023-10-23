import os

ROOT_PATH = os.getcwd()
MODEL_VERSION = "0.0.1"
LOCAL_OBJECTS_PATH = os.path.join(ROOT_PATH, "src/web_service/local_objects")
MODEL_PATH = os.path.join(LOCAL_OBJECTS_PATH, "model.pkl")
PREPROCESSOR_PATH = os.path.join(LOCAL_OBJECTS_PATH, "numerical_encoders.pkl")
LABEL_ENCODER_PATH = os.path.join(LOCAL_OBJECTS_PATH, "label_encoders.pkl")
CATEGORICAL_VARS = ["Sex"]
NUMERICAL_COLS = ["Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight"]
ROOT_PATH = os.getcwd()

# MISC
APP_TITLE = "AbaloneAgePredictionApp"
APP_DESCRIPTION = (
    "A simple API to predict Abalone Age" "given some abalone morphometrics measurements. "
)
APP_VERSION = "0.0.1"
