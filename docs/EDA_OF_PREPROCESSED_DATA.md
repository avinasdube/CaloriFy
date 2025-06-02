# For proper EDA of Preprocessed Data

## Step 1: Load the Dataset Properly
    This tells you what’s inside: images, category, class_names, etc.

## Step 2: Extract and Inspect the Data
    - Load and examine each part and print few values.
    - Understand the shape and type of images and labels.

## Step 3: Visualize Sample Images and Labels
    - Plot images with their decoded class names to understand what's in the dataset.
    - Confirms that your data is not corrupted.
    - Helps you see the images and what labels they correspond to.
    - Ensures that label mappings work correctly.

## Step 4: Understand the Label Distribution
    Find out how often each food class appears. This helps you understand which classes dominate and if the data is imbalanced.

    Since your labels are one-hot encoded, we need to:

    - Convert each one-hot vector into its class index
    - Count how often each class appears
    - Plot the class distribution

    What to Look For

    - Equal bar heights → balanced dataset ✅
    - Some bars much smaller → imbalance ❗
        - In such cases, you may need resampling or class weighting during model training

## Step 5: Check Multi-Label Nature
    See how many labels each image typically has. This confirms that this is a multi-label dataset, not single-label.

    This step helps you confirm how the category labels are stored. For classification tasks:

    - One-hot encoded labels look like:
      [0, 0, 1, 0, 0, ..., 0] → exactly one 1, rest are 0s

    - Multi-label would have multiple 1s like:
      [0, 1, 0, 1, ..., 0]

## Step 6: Preprocess Images for Modeling
    You should:

    - Normalize images: images = images / 255.0
    - Convert labels to float32 for most ML frameworks
    - Split into train/test/validation

## Step 7: Prepare for Deep Learning Framework
    Depending on your library (TensorFlow or PyTorch), wrap the data into:

    - TensorFlow: tf.data.Dataset
    - PyTorch: Custom Dataset and DataLoader

## Step 8: (Optional) Map Class to Calories
    If your project is food calorie prediction, you’ll need:

    - A CSV or dictionary mapping class_name → average_calories
    - Then for each image, you can assign a calorie label based on the predicted class
