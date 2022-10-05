import pandas as pd

def load_csv_to_df(filename, sep=','):
    df = pd.read_csv(filename, sep=sep, index_col=0)
    return df
