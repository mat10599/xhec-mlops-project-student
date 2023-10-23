import os
import pickle
import logging
from functools import lru_cache

from loguru import logger

logger = logging.getLogger(__name__)

@lru_cache  
def load_model(filepath: os.PathLike):
    logger.info(f"Loading model from {filepath}")
    try:
        with open(filepath, "rb") as f:
            model = pickle.load(f)
        logger.info(f"Model loaded successfully from {filepath}")
        return model
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        
    except Exception as e:
        logger.error(f"An error occurred while loading the model: {e}")



@lru_cache 
def load_preprocessor(filepath: os.PathLike):
    logger.info(f"Loading preprocessor from {filepath}")

    try:
        with open(filepath, "rb") as f:
            preprocessor = pickle.load(f)
        logger.info(f"Preprocessor loaded successfully from {filepath}")
        return preprocessor

    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")

    except pickle.UnpicklingError:
        logger.error(f"File {filepath} could not be unpickled.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

