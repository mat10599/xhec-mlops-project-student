# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.
from preprocessing import preprocessing
from training import train_model
import argparse
from utils import read_data
from pathlib import Path


def main(trainset_path: Path) -> None:
    """main function to train the model and save it in pkl format in the `src/web_service/local_objects` folder.
    standard scaler and label encoder are also saved in the same folder.

    Args:
        trainset_path (Path): path to the training set
    """
    # Read data
    raw_data = read_data(trainset_path)
    # Preprocess data
    preprocessed_df = preprocessing(raw_data, training=True)
    # (Optional) Pickle encoder if need be

    # Train model
    train_model(preprocessed_df)
    # Pickle model --> The model should be saved in pkl format the `src/web_service/local_objects` folder


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
    # main(Path("data/abalone.csv"))
