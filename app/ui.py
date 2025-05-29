# import streamlit as st
# from PIL import Image
# import pandas as pd
# import numpy as np
# from src.pipeline import predict_calories

# st.title("CaloriFy: Food Calorie Predictor")

# st.sidebar.header("Upload Image")
# uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption='Uploaded Image.', use_column_width=True)
#     st.write("")
#     st.write("Classifying...")

#     # Call the prediction function from the pipeline
#     calories = predict_calories(uploaded_file)

#     st.write(f"Estimated Calories: {calories} kcal per 100g")

# st.sidebar.header("Calorie Mapping")
# calorie_mapping = pd.read_csv('data/calorie_mapping.csv')
# st.sidebar.dataframe(calorie_mapping)
