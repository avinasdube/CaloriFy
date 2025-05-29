# import pytest
# from app.ui import app

# @pytest.fixture
# def client():
#     app.testing = True
#     with app.test_client() as client:
#         yield client

# def test_home_page(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert b'CaloriFy' in response.data

# def test_upload_image(client):
#     with open('data/test_images/sample_image.jpg', 'rb') as img:
#         response = client.post('/upload', data={'file': img})
#     assert response.status_code == 200
#     assert b'Prediction' in response.data

# def test_calorie_prediction(client):
#     response = client.get('/predict?food_name=apple')
#     assert response.status_code == 200
#     assert b'Calories per 100g' in response.data

# def test_invalid_image_upload(client):
#     response = client.post('/upload', data={'file': ''})
#     assert response.status_code == 400
#     assert b'No file uploaded' in response.data
