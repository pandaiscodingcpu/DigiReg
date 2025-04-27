import numpy as np
import cv2 as cv
import os
import joblib
import matplotlib.pyplot as plt

# Load the saved model using joblib
rf_cf = joblib.load('digireg.joblib')

folder_path = './Digits'  # Folder where your resized digit images are stored
predictions = []

# Iterate through all the images in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg','.png')):
        file_path = os.path.join(folder_path, filename)

        # Read the image
        img = cv.imread(file_path)

        # Convert image to grayscale
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Resize to 28x28 pixels, use nearest-neighbor interpolation
        resized = cv.resize(gray, (28, 28), interpolation=cv.INTER_NEAREST)

        # Normalize the pixel values to [0, 1] by dividing by 255 (since model expects this)
        resized_normalized = resized / 255.0

        # Flatten the image to 1D array
        flattened_image = resized_normalized.flatten()

        # Predict using the loaded model
        y_pred = rf_cf.predict([flattened_image])

        # Store predictions
        predictions.append((filename, y_pred[0]))

        # Display the image and the predicted digit
        plt.imshow(resized, cmap='gray')
        plt.title(f"Predicted Digit: {y_pred[0]}")
        plt.show()

# Print all predictions after processing the folder
for filename, prediction in predictions:
    print(f"Image: {filename} -> Predicted Digit: {prediction}")
