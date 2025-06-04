# eda/visualize_data.py
'''
    Sample visualizations like random image grids or label distributions.
'''

import matplotlib.pyplot as plt
import numpy as np
from eda.data_loader import load_dataset

def show_random_images(num_samples=5):
    images, labels, label_names = load_dataset()
    label_map = {i: name.decode() for i, name in enumerate(label_names[:])}

    plt.figure(figsize=(12, 5))
    for i in range(num_samples):
        idx = np.random.randint(0, len(images))
        img = images[idx]
        label = np.argmax(np.array(labels[idx]))
        class_name = label_map[label]

        plt.subplot(1, num_samples, i + 1)
        plt.imshow(img.astype('uint8'))
        plt.title(f"{class_name} ({label})", fontsize=10)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

