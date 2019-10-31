import os


from src.utils import pathfinder

root = pathfinder.find_root()

# Data
TRAIN_DATA_PATH = os.path.join(root, r'data/train_data.csv')

