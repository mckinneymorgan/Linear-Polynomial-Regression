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
print("Data:")
print(data)

featureCount = len(data[0])-1
print("Features:")
print(featureCount)



