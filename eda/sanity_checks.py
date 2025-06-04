# eda/sanity_checks.py
'''
    Data validation: NaNs, invalid shapes, out-of-bound labels.
'''

import numpy as np
from eda.data_loader import load_dataset
from eda.config import NUM_CLASSES

def run_sanity_checks():
    images, labels, _ = load_dataset()

    # CHECK NaNs
    if np.isnan(images).any():
        print("Warning: NaNs found in images.")
    else:
        print("No, NaNs found in images.")


    # CHECK FOR LABEL BOUNDS
    if labels.min() < 0 or labels.max() >= NUM_CLASSES:
        print(f"Labels out of bounds: {labels.min()} to {labels.max()}")
    else:
        print("All labels in valid range.")

