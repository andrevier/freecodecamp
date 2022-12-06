# book: Hands-on Machine Learning with Scikit-learn, Keras, and 
# TensorFlow. 2nd ed. page 401
# Building complex models with functional API: Wide and Deep MLP.

from sklearn.datasets import fetch_california_housing as californiaHousing
from sklearn.model_selection import train_test_split as trainTestSplit
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt

# Get California housing dataset.
housing = californiaHousing()

# Separate the dataset into trainning and testing data.
xTrainFull, xTest, yTrainFull, yTest = trainTestSplit(
    housing.data, housing.target 
    )

# Separate the trainning data into train and validation data.
xTrain, xValid, yTrain, yValid = trainTestSplit(
    xTrainFull, yTrainFull
    )

# data content
print("housing data type " + str(housing))
print("")
print("Full trainning data: " + str(xTrainFull.shape))
print("Test data: " + str(xTest.shape))
print("Target trainning data: " + str(yTrainFull.shape))
print("")
print("Trainning data after validation set partition: " + str(xTrain.shape))
print("Validation data: " + str(xValid.shape))
print("")

# Sequential model 
model = keras.models.Sequential([
    keras.layers.Dense(30, activation="relu", input_shape=xTrain.shape[1:]),
    keras.layers.Dense(1)
])

# # Build the MLP with functional API: fig10_14.jpg
# input_ = keras.layers.Input(shape=xTrain.shape[1:])
# hidden1 = keras.layers.Dense(30, activation="relu")(input_)
# hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)
# concat = keras.layers.Concatenate()([input_, hidden2])
# output = keras.layers.Dense(1)(concat)
# model = keras.Model(inputs=[input_], outputs=[output])

# Compile 
model.compile(loss="mean_squared_error",
    optimizer=keras.optimizers.SGD(lr=0.1),
    metrics=["accuracy"])

history = model.fit(xTrain, yTrain, epochs=20, 
                    validation_data=(xValid, yValid))

# # Plot the loss and accuracy
# pd.DataFrame(history.history).plot(figsize=(8, 5))
# plt.grid(True)
# plt.gca().set_ylim(0, 1) # set the vertical range to [0-1]
# plt.show()

MSETest = model.evaluate(xTest, yTest)
print("MSE of the test: "  + str(MSETest))