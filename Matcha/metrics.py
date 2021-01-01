import pandas as pd
import numpy as np


def calculate_accuracy(df: pd.DataFrame) -> float:
    """Compute PLR accuracy from historical matches.
    """
    if ('winner' not in df.columns) or ('loser' not in df.columns):
        raise ValueError("Missing columns in dataframe.")

    correct = np.sum(df['winner'] >= df['loser'])
    return correct / df.shape[0]
