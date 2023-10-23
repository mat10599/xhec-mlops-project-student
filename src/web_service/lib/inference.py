from typing import List
import numpy as np
import pandas as pd
import logging 
from sklearn.base import BaseEstimator
from lib.models import InputData
from lib.preprocessing import preprocessing

logger = logging.getLogger(__name__)

def run_inference(input_data: List[InputData], ss, label_encoder, model: BaseEstimator) -> np.ndarray:
    """Run inference on a list of input data.

    Args:
        Abalone_data (dict): the data point to run inference on.
        ss (StandardScaler): the SdandardScaler object.
        model (BaseEstimator): the fitted model object.

    Returns:
        np.ndarray: the predicted Abalone age in years.

    Example Abalone_data:
        {'Sex':F,	'Length':0.455,	'Diameter':0.365,	'Height':0.095,	'Whole weight':0.5140,	'Shucked weight':0.2245,	'Viscera weight':0.1010,	'Shell weight':0.150}
    """

    logger.info(f"Running inference on:\n{input_data}")
    df = pd.DataFrame([x.dict() for x in input_data])
    
    processed_df = preprocessing(df, ss, label_encoder)

    y = model.predict(processed_df)
    logger.info(f"Predicted Abalone age:\n{y}")
    return y
