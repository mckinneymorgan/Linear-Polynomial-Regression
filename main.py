# Original author: Morgan McKinney 3/2021

import read
import csv

# Initialize variables
names = []
classValueName = "class value"
data = []
classValues = []

# User input, read and store input csv file
print("LINEAR AND POLYNOMIAL REGRESSION \n")
read.read_file(names, classValueName, data, classValues)
print(data)
