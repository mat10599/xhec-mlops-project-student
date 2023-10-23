# MODELS
MODEL_VERSION = "0.0.1"
PREPROCESSOR_FUNCT_NAME = ""
MODEL_NAME = ""
PATH_TO_PREPROCESSOR = f"local_models/{PREPROCESSOR_FUNCT_NAME}__v{MODEL_VERSION}.pkl"
PATH_TO_MODEL = f"local_models/{MODEL_NAME}__v{MODEL_VERSION}.pkl"
CATEGORICAL_VARS = ["Sex"]


# MISC
APP_TITLE = "AbaloneAgePredictionApp"
APP_DESCRIPTION = (
    "A simple API to predict Abalone Age"
    "given some abalone morphometrics measurements. "
)
APP_VERSION = "0.0.1"