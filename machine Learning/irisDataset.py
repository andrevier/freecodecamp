# book: Hands-on Machine Learning with Scikit-learn, Keras, and TensorFlow
# 2nd ed. page 374
# Trainning a perceptron with the iris dataset.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import Perceptron


# Get the iris dataset.
iris = datasets.load_iris()

# Meta data from the dataset.
#print(iris["DESCR"])

# Get the petal length and petal width.
X = iris.data[:,(2,3)]

# Select all the iris setosa class (target equals to 0) and extract as
# a list of 1's and 0's.
y = (iris.target == 0).astype(int)

perceptron = Perceptron()
perceptron.fit(X, y)
setosaPrediction = perceptron.predict([[1.5, 0.2]])
print(setosaPrediction)







