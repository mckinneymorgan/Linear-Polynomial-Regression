# Original author: Morgan McKinney 3/2021

import read
import regression

# Initialize variables
names = []
classValueName = ""
data = []
classValues = []

# User input, read and store input csv file
print("LINEAR AND POLYNOMIAL REGRESSION \n")
read.read_file(names, classValueName, data, classValues)
featureCount = len(data[0])-1
newFeatureValues = [[y for y in x] for x in data]

print("Data:")
print(data)
print("Features:")
print(featureCount)
print("New feature values:")
print(newFeatureValues)





