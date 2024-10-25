# -*- coding: utf-8 -*-
"""disease.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vcvgw1sOJUCpJoJejZHArU04uJsYalao
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

from google.colab import drive
import zipfile
import os

"""drive.mount('/content/drive/MyDrive/tea leaf dataset')"""

drive.mount('/content/drive')

dataset_zip = '/content/drive/MyDrive/dataset.zip'  # Replace with your zip file location

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from google.colab import drive
import zipfile
import os

# Mount Google Drive
drive.mount('/content/drive')

# Set dataset paths
dataset_path = '/content/drive/MyDrive/tea leaf dataset'
train_dir = os.path.join(dataset_path, 'train')
validation_dir = os.path.join(dataset_path, 'validation')

# Define model parameters
IMG_HEIGHT, IMG_WIDTH = 224, 224  # Image dimensions
BATCH_SIZE = 32
EPOCHS = 20
LEARNING_RATE = 0.001

# Data Augmentation and Preprocessing
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255.0,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

validation_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

import os

dataset_path = '/content/drive/MyDrive/tea leaf dataset'
print("Contents of the dataset directory:", os.listdir(dataset_path))

from google.colab import drive
drive.mount('/content/drive')

dataset_path = '/content/drive/MyDrive/tea_leaf_dataset'
train_dir = os.path.join(dataset_path, 'train')
validation_dir = os.path.join(dataset_path, 'validation')

# Import necessary libraries
import os
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Set the base dataset path
dataset_path = '/content/drive/MyDrive/tea leaf dataset'

# List the contents of the base dataset path
print("Contents of the dataset directory:", os.listdir(dataset_path))

# Check the contents of the 'tea leaf dataset' directory
print("Contents of the 'tea leaf dataset':", os.listdir(dataset_path))

# Check if the 'train' and 'validation' folders exist
train_dir = os.path.join(dataset_path, 'train')
validation_dir = os.path.join(dataset_path, 'validation')

print("Train directory exists:", os.path.exists(train_dir))
print("Validation directory exists:", os.path.exists(validation_dir))

# If train directory exists, list its contents
if os.path.exists(train_dir):
    print("Contents of the train directory:", os.listdir(train_dir))

# If validation directory exists, list its contents
if os.path.exists(validation_dir):
    print("Contents of the validation directory:", os.listdir(validation_dir))

# Create directories if they don't exist
if not os.path.exists(train_dir):
    os.makedirs(train_dir)
    print("Created train directory.")

if not os.path.exists(validation_dir):
    os.makedirs(validation_dir)
    print("Created validation directory.")

# Data augmentation and preprocessing
train_datagen = ImageDataGenerator(rescale=1.0 / 255.0)
validation_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

# Load data from directories
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),  # Image dimensions
    batch_size=32,
    class_mode='categorical'
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# Build the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(train_generator.num_classes, activation='softmax')  # Output layer for each disease class
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=LEARNING_RATE),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

from tensorflow.keras import layers, models

# Get the number of classes from the train generator
num_classes = train_generator.num_classes

# Example of a simple Convolutional Neural Network (CNN)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax')  # Make sure num_classes matches your dataset
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Get a batch of training data
x_batch, y_batch = next(train_generator)

print("Batch shape:", x_batch.shape)  # Should show (BATCH_SIZE, IMG_HEIGHT, IMG_WIDTH, 3)
print("Labels shape:", y_batch.shape)  # Should show (BATCH_SIZE, num_classes)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical'  # For multiple classes
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

from tensorflow.keras import layers, models

# Get the number of classes from the train generator
num_classes = train_generator.num_classes

# Example of a simple Convolutional Neural Network (CNN)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax')  # Make sure num_classes matches your dataset
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',  # Use categorical_crossentropy for multi-class
              metrics=['accuracy'])

# Ensure the input shape is correct
# input_shape should match the shape of your images
input_shape = (IMG_HEIGHT, IMG_WIDTH, 3)

# Check the batch shape
x_batch, y_batch = next(train_generator)

# Check if the input shape matches the batch shape
assert x_batch.shape[1:] == input_shape, f"Input shape mismatch. Model expects {input_shape}, but got {x_batch.shape[1:]}"

# Save the trained model
model.save('/content/drive/MyDrive/tea_leaf_disease_model.h5')
print("Model training complete and saved to Google Drive.")