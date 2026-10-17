# Matplot , Seaborn & Tensorflow

# 1. Matplot
print("Matplotlib")
import matplotlib.pyplot as plt

students = ["Ali", "Ahmed", "Sara", "Ayesha"]
marks = [85, 70, 90, 78]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()



# Seaborn

print("Seaborn")

import seaborn as sns
import matplotlib.pyplot as plt

students = ["Ali", "Ahmed", "Sara", "Ayesha"]
marks = [85, 70, 90, 78]

sns.barplot(x=students, y=marks)

plt.title("Student Marks Using Seaborn")
plt.show()


#TensorFlow Overview
#TensorFlow is an open-source machine learning framework developed by Google. It helps us build, train, and use machine learning and deep learning models.
# For example, TensorFlow can help build systems that recognize images, predict house prices, detect fraud, or understand text.

import tensorflow as tf
import numpy as np

# Training data
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Build a neural network
model = tf.keras.Sequential([
    tf.keras.Input(shape=[1]),
    tf.keras.layers.Dense(units=1)
])

# Configure the training process
model.compile(
    optimizer="sgd",
    loss="mean_squared_error"
)

# Train the model
model.fit(X, y, epochs=300, verbose=0)

# Make a prediction
prediction = model.predict(
    np.array([6.0]),
    verbose=0
)

print("Prediction:", prediction[0][0])