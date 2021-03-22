# Original author: Morgan McKinney 3/2021

import read
import regression
import numpy as np
import matplotlib.pyplot as plt

# Initialize variables
names = []
classValueName = ""
data = []
classValues = []
alpha = 0.001

# User input, read and store input csv file
print("LINEAR AND POLYNOMIAL REGRESSION \n")
read.read_file(names, classValueName, data, classValues)
data = np.array(data)  # Store data column-wise
featureCount = len(data[0])-1
newFeatureValues = [[y for y in x] for x in data]

print("Data:")
print(data)
print("Features:")
print(featureCount)
print("New feature values:")
print(newFeatureValues)

# Plot data
x = []
y = []
plt.title("Linear Regression")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x, y, color="green")
plt.show()





