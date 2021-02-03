import pandas as pd


def print_dim(df: pd.DataFrame):
    x, y = df.shape
    print(f"This DataFrame contains {x} rows and {y} columns")