# import pandas as pd
# import pickle
# from sklearn.linear_model import LinearRegression

# class CalorieRegressor:
#     def __init__(self, model_path):
#         self.model = self.load_model(model_path)

#     def load_model(self, model_path):
#         with open(model_path, 'rb') as file:
#             model = pickle.load(file)
#         return model

#     def predict_calories(self, features):
#         return self.model.predict(features)

#     def evaluate_model(self, X_test, y_test):
#         predictions = self.predict_calories(X_test)
#         mse = ((predictions - y_test) ** 2).mean()
#         return mse

#     def get_calorie_mapping(self, csv_path):
#         return pd.read_csv(csv_path)
