# Original author: Morgan McKinney 3/2021

import read
import regression
import sys
from random import random
import numpy as np
import matplotlib.pyplot as plt

# Initialize variables
names = []
data = []
alpha = 0.001
epochMax = 100
linear = True
order = 11  # Number of features in synthetic dataset, default

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
dataNew = data.copy()
if not linear:
    example = 0
    newIndex = 0
    for x in range(order):  # Expand array to allow for more indexes
        newIndex += 1
        dataNew = np.insert(dataNew, newIndex, 0, axis=1)
    for m in data:
        index = 0
        original = dataNew[example][index]
        for x in range(order):  # Assign casted values in new index
            index += 1
            cast = float(original) ** (index + 1)
            dataNew[example][index] = cast
        example += 1

# Output given information
featureCountOriginal = len(data[0])-1
featureCount = len(dataNew[0])-1
print("Original features: " + str(featureCountOriginal))
print("Features: " + str(featureCount))
print("Order: " + str(order))
print(dataNew)

# Set initial weights
weights = []
for x in range(order + 1):
    weights.append(random())  # Random float from 0 to 1
weights = np.array(weights)

# Regression
epoch = 1
while epoch <= epochMax:
    meanSquaredError = []
    example = 0
    for m in dataNew:
        entry = np.array(dataNew[example])
        featuresOnly = entry[:-1].copy()
        inputs = np.insert(featuresOnly, 0, 1.0)  # x_0 = 1, always
        hypothesis = np.dot(np.transpose(weights), inputs)  # Scalar
        groundTruth = dataNew[example][featureCount]
        rawError = hypothesis - groundTruth  # Scalar
        gradient = rawError * inputs  # 1 x n
        # Output variables
        # print("Inputs: " + str(inputs))
        # print("Weights: " + str(weights))
        # print("Hypothesis: " + str(hypothesis))
        # print("Ground truth: " + str(groundTruth))
        # print("Raw error: " + str(rawError))
        # print("Gradient: " + str(gradient))
        # Weight updates
        weightsTemp = weights.copy()
        feature = 0
        for n in weights:
            print(weights[feature])
            weights[feature] = weightsTemp[feature] - alpha * gradient[feature]
            feature += 1
        # Find squared error for data entry
        mse = np.dot(np.transpose(weights), inputs)
        mse = mse - groundTruth
        meanSquaredError.append(mse)
        example += 1
    # Find average squared error over all data
    averageSquaredError = sum(meanSquaredError) / len(meanSquaredError)
    print("MSE after " + str(epoch) + " iterations: " + str(averageSquaredError))
    epoch += 1

# Plot data
if not linear:  # Only works for polynomial regression
    x1 = [i[0] for i in data]  # First column
    y1 = [i[featureCountOriginal] for i in data]  # Ground truth column
    x2 = x1
    y2 = []  # Prediction
    example = 0
    for m in dataNew:
        entry = np.array(dataNew[example])
        featuresOnly = entry[:-1].copy()
        inputs = np.insert(featuresOnly, 0, 1.0)  # x_0 = 1, always
        y2.append(np.dot(np.transpose(weights), inputs))  # Scalar
        example += 1
    plt.title("Linear Regression")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.scatter(x1, y1, color="blue")  # Actual data
    plt.plot(x2, y2, color="red")  # Model prediction
    plt.show()





