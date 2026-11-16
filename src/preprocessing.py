import pandas as pd
import numpy as np

def explore_data(df):
    """
    Display basic information about the dataset.
    """

    print("Dataset shape:")
    print(df.shape)

    print("\nDataset information:")
    print(df.info())

    print("\nMissing values:")
    print(df.isnull().sum())

    return df
