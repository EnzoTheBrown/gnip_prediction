import pandas as pd
from gnip.models.store import load_dataset


def get_data_from_type(type):
    filename = load_dataset()
    df = pd.read_csv(filename, delimiter='\t')
    df = df[df['type'] == type]

    return df
