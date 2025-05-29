# import os
# import pandas as pd
# from src.image_preprocessing import preprocess_image
# from src.food_classifier import FoodClassifier
# from src.calorie_regressor import CalorieRegressor

# class CaloriFyPipeline:
#     def __init__(self, calorie_mapping_path, model_paths):
#         self.calorie_mapping = pd.read_csv(calorie_mapping_path)
#         self.food_classifier = FoodClassifier(model_paths['food_classifier'])
#         self.calorie_regressor = CalorieRegressor(model_paths['calorie_regressor'])

#     def process_image(self, image_path):
#         processed_image = preprocess_image(image_path)
#         return processed_image

#     def predict_food(self, image_path):
#         processed_image = self.process_image(image_path)
#         food_prediction = self.food_classifier.predict(processed_image)
#         return food_prediction

#     def predict_calories(self, food_name):
#         calories_per_100g = self.calorie_mapping.loc[self.calorie_mapping['food_name'] == food_name, 'calories_per_100g']
#         if not calories_per_100g.empty:
#             return calories_per_100g.values[0]
#         else:
#             return None

#     def run_pipeline(self, image_path):
#         food_name = self.predict_food(image_path)
#         calories = self.predict_calories(food_name)
#         return food_name, calories

# if __name__ == "__main__":
#     calorie_mapping_path = os.path.join('data', 'calorie_mapping.csv')
#     model_paths = {
#         'food_classifier': os.path.join('models', 'food_classifier.h5'),
#         'calorie_regressor': os.path.join('models', 'calorie_regressor.pkl')
#     }
#     pipeline = CaloriFyPipeline(calorie_mapping_path, model_paths)
#     # Example usage
#     # food_name, calories = pipeline.run_pipeline('path_to_image.jpg')
#     # print(f"Predicted food: {food_name}, Calories: {calories}")
