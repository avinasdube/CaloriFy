# import numpy as np
# import pandas as pd
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.image import img_to_array, load_img

# class FoodClassifier:
#     def __init__(self, model_path, class_labels):
#         self.model = load_model(model_path)
#         self.class_labels = class_labels

#     def preprocess_image(self, image_path, target_size=(224, 224)):
#         image = load_img(image_path, target_size=target_size)
#         image = img_to_array(image)
#         image = np.expand_dims(image, axis=0) / 255.0
#         return image

#     def predict(self, image_path):
#         processed_image = self.preprocess_image(image_path)
#         predictions = self.model.predict(processed_image)
#         predicted_class = self.class_labels[np.argmax(predictions)]
#         confidence = np.max(predictions)
#         return predicted_class, confidence

#     def evaluate(self, test_images):
#         results = []
#         for image_path in test_images:
#             predicted_class, confidence = self.predict(image_path)
#             results.append((image_path, predicted_class, confidence))
#         return results
