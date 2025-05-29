# from flask import Flask, request, jsonify
# from src.pipeline import predict_calories

# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     image_path = data.get('image_path')

#     if not image_path:
#         return jsonify({'error': 'No image path provided'}), 400

#     try:
#         calories = predict_calories(image_path)
#         return jsonify({'calories': calories}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
