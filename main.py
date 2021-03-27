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

# Set initial weights
weights = []
for x in range(order + 1):
    weights.append(random())  # Random float from 0 to 1
weights = np.array(weights)

# Basis expansion

# Output given information
featureCount = len(data[0])-1
print("Features: " + str(featureCount))
print("Order: " + str(order))
print(data)

# Regression
epoch = 1
while epoch <= epochMax:
    meanSquaredError = []
    example = 0
    for m in data:
        entry = np.array(data[example])
        featuresOnly = entry[:-1].copy()
        inputs = np.insert(featuresOnly, 0, 1.0)  # x_0 = 1, always
        hypothesis = np.dot(np.transpose(weights), inputs)  # Scalar
        groundTruth = data[example][featureCount]
        rawError = hypothesis - groundTruth  # Scalar
        gradient = rawError * inputs  # 1 x n
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
    y1 = [i[featureCount] for i in data]  # Ground truth column
    x2 = x1
    y2 = []  # Prediction
    example = 0
    for m in data:
        entry = np.array(data[example])
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





