# eda/analyze_dataset.py
'''
    Basic information and structure of the dataset.
'''

import numpy as np
from eda.data_loader import load_dataset

def print_basic_info():
    images, labels, _ = load_dataset()
    print("Images Shape: ", images.shape)
    print("Labels Shape: ", labels.shape)
    print("Unique Labels: ", len(np.unique(labels)))
