import pandas as pd

def drop_record(olympics: pd.Series):
    return olympics.drop(index=2020)