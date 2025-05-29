# CaloriFy Project

CaloriFy is a comprehensive application designed to classify food images and predict their calorie content. This project utilizes deep learning techniques to provide users with nutritional information based on food images.

## Project Structure

The project is organized into several directories and files, each serving a specific purpose:

- **data/**: Contains all datasets and mappings.
  - **raw/**: Original images or datasets (e.g., Food-101).
  - **processed/**: Resized, cleaned, and split data.
  - **calorie_mapping.csv**: CSV file mapping food names to their calorie content per 100g.
  - **test_images/**: Images used for testing predictions.

- **models/**: Holds the trained model weights.
  - **food_classifier.h5**: Saved CNN model for food classification.
  - **calorie_regressor.pkl**: Saved regression model for calorie prediction.

- **notebooks/**: Jupyter notebooks for exploration and prototyping.
  - **01_data_preprocessing.ipynb**: Data preprocessing tasks.
  - **02_food_classification.ipynb**: Food classification techniques.
  - **03_calorie_regression.ipynb**: Calorie regression techniques.

- **src/**: Core project source code.
  - **__init__.py**: Marks the directory as a Python package.
  - **config.py**: Constants, paths, and hyperparameters.
  - **image_preprocessing.py**: Functions for image resizing, normalization, and augmentations.
  - **food_classifier.py**: Functions to load, train, and predict using the CNN model.
  - **calorie_regressor.py**: Functions related to the regression model.
  - **utils.py**: Shared utility functions (label encoding, logging, etc.).
  - **pipeline.py**: Full pipeline: image → calories.

- **app/**: Application interface (Streamlit or Flask).
  - **__init__.py**: Marks the directory as a Python package.
  - **ui.py**: Streamlit UI code.
  - **api.py**: (Optional) Flask or FastAPI backend.

- **tests/**: Manual and automated testing.
  - **test_pipeline.py**: Tests for the prediction pipeline.
  - **test_ui.py**: UI test cases (if needed).

- **assets/**: Static files for UI (icons, example images).
  - **logo.png**: Logo image for the UI.

- **saved_outputs/**: Logs, predictions, charts.
  - **predictions.csv**: Stores logs and predictions.
  - **evaluation_plots/**: Contains evaluation plots (e.g., confusion matrix, actual vs. predicted).

- **requirements.txt**: Project dependencies.

- **README.md**: Project overview and instructions.

- **.gitignore**: Specifies files and directories to be ignored by version control.

- **run_app.py**: Entry point to launch the application.

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd CaloriFy
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```bash
python run_app.py
```

This will start the application, allowing you to upload food images and receive calorie predictions.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.