# Original author: Morgan McKinney 3/2021

import read
import regression
import sys
from random import randint
import numpy as np
import matplotlib.pyplot as plt

# Initialize variables
names = []
classValueName = ""
data = []
classValues = []
alpha = 0.001
epochMax = 100
linear = True
order = 11  # Number of features in synthetic dataset, default
predictions = []

# User input, read and store input csv file
print("LINEAR AND POLYNOMIAL REGRESSION \n")
read.read_file(names, data)
data = np.array(data)  # Store data row-wise
regressionType = input("Linear or polynomial regression? ")
if regressionType.lower() == 'polynomial' or regressionType.lower() == 'poly':
    linear = False
    orderStr = input("What is the order? ")
    order = int(orderStr)
elif regressionType.lower() != 'linear':
    sys.exit("Invalid input")

# Basis expansion
order += 1
weights = [0] * order
theta_0 = randint(0, 1)
theta_1 = randint(0, 1)

# Output given information
print("Data:")
print(data)
featureCount = len(data[0])-1
print("Features:")
print(featureCount)
print("New feature values:")
print(newFeatureValues)

# Stochastic gradient descent
for x in data:
    h = regression.weight_update(data, alpha)
    predictions.append()

epoch = 1
while epoch <= epochMax:
    meanSquaredError = []
    for m in data:
        inputs = data[m]
        inputs.insert(0, 1)
        hypothesis = regression.get_h_theta(weights, inputs)
        gradient = rawError * inputs
        mse =
        meanSquaredError.append(mse)
    averageSquaredError = sum(meanSquaredError) / m
    print("MSE after " + epoch + " iterations: " + averageSquaredError)
    epoch += 1

# Plot data
if not linear:  # Only works for polynomial regression
    x = [i[0] for i in data]  # First column
    y = [i[featureCount] for i in data]  # Prediction column
    plt.title("Linear Regression")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.scatter(x, y, color="green")
    plt.show()





