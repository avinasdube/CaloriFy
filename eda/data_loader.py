# eda/data_loader.py
'''
    Loads the .h5 dataset from disk and returns arrays.
'''

import h5py
import numpy as np
from eda.config import HDF5_DATASET_PATH

def load_dataset():
    with h5py.File(HDF5_DATASET_PATH, 'r') as f:
        images = np.array(f['images'])
        labels = np.array(f['category'])
        label_names = np.array(f['category_names'])
    return images, labels, label_names
