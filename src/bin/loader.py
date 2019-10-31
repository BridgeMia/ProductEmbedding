import pandas as pd

from src.constants import TRAIN_DATA_PATH


def load_train(fp=None):
    if not fp:
        fp = TRAIN_DATA_PATH
    return pd.read_csv(fp)

