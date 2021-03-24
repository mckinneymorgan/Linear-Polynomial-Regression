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
epochMax = 100  # Full batch
theta_0 = randint(0, 1)
theta_1 = randint(0, 1)
theta = [theta_0, theta_1]
linear = True
order = 11  # Number of features in synthetic dataset, default

# User input, read and store input csv file
print("LINEAR AND POLYNOMIAL REGRESSION \n")
read.read_file(names, data)
data = np.array(data)  # Store data column-wise
regressionType = input("Linear or polynomial regression? ")
if regressionType.lower() == 'polynomial' or regressionType.lower() == 'poly':
    linear = False
    orderStr = input("What is the order? ")
    order = int(orderStr)
elif regressionType.lower() != 'linear':
    sys.exit("Invalid input")

featureCount = len(data[0])-1
newFeatureValues = [[y for y in x] for x in data]

print("Data:")
print(data)
print("Features:")
print(featureCount)
print("New feature values:")
print(newFeatureValues)

# Plot data
if not linear:  # Only works for polynomial regression
    x = [i[0] for i in data]  # First column
    y = [i[featureCount] for i in data]  # Prediction column
    plt.title("Linear Regression")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.scatter(x, y, color="green")
    plt.show()





