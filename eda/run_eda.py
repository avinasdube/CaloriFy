# eda/run_eda.py
'''
    Main script to run all EDA steps together.
'''

from eda.analyze_dataset import print_basic_info
from eda.visualize_data import show_random_images
from eda.sanity_checks import run_sanity_checks

if __name__ == "__main__":
    print("=== Dataset Info ===")
    print_basic_info()

    print("\n=== Random Image Samples ===")
    show_random_images(num_samples=5)

    print("\n=== Sanity Checks ===")
    run_sanity_checks()
