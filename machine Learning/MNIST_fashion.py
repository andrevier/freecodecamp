# book: Hands-on Machine Learning with Scikit-learn, Keras, and 
# TensorFlow. 2nd ed. page 384
# MNIST fashion data and trainning a MLP for classification with
# sequential method.

import tensorflow as tf
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
print(X_train_full.shape)

# Separate the trainning set into 2: trainning set and validation set
# The gray scale of the images goes from 0 to 255. We also transform 
# the scale into the interval [0,1] for better trainning with gradient
# descent.
X_valid, X_train = X_train_full[:5000]/255.0, X_train_full[5000:]/255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
print(y_train[0])
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28,28]),
    keras.layers.Dense(300, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
    ])

# Compile the model
model.compile(loss="sparse_categorical_crossentropy",
    optimizer=keras.optimizers.SGD(lr=0.1),
    metrics=["accuracy"]
    )

# Train the model with fit method.
history = model.fit(X_train, y_train, epochs=30,
                    validation_data=(X_valid, y_valid))

# Plot the loss and accuracy
pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1) # set the vertical range to [0-1]
plt.show()
