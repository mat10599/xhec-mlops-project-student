import pandas as pd 
from sklearn.preprocessing import LabelEncoder


def preprocessing(dataset_path: str)->pd.DataFrame:
    df = read_data(dataset_path=dataset_path)
    df['age'] = df['Rings']+1.5
    df = df.drop('Rings', axis = 1)
    label_encoder = LabelEncoder()
    df['Sex'] = label_encoder.fit_transform(df['Sex'])
    return df



def read_data(dataset_path: str) -> pd.DataFrame:
    """Read the data at the given path and return a dataframe."""
    df = pd.read_csv(dataset_path)
    return df