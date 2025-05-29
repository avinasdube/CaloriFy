# import cv2
# import numpy as np

# def resize_image(image, target_size=(224, 224)):
#     return cv2.resize(image, target_size)

# def normalize_image(image):
#     return image / 255.0

# def augment_image(image):
#     # Example augmentation: random horizontal flip
#     if np.random.rand() > 0.5:
#         image = np.fliplr(image)
#     return image

# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     image = resize_image(image)
#     image = normalize_image(image)
#     image = augment_image(image)
#     return image
