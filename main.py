# Original author: Morgan McKinney 3/2021

import csv

# User input, get filename(s)
print("LINEAR AND POLYNOMIAL REGRESSION \n")
file = input("Enter csv file name: ")
classValueFileExist = False
classValueFile = input("Are the class labels in another file (Y/N): ")
if classValueFile.lower() == 'y':
    classValueFile = input("Enter class label file name: ")
    classValueFileExist = True
featureNames = False
featureNamesExist = input("Are the features named (Y/N): ")
if featureNamesExist.lower() == 'y':
    featureNames = True

# Read file
names = []
data = []
classValueName = 0
classValues = []
with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # Count features, return to start of file
    featureCount = len(next(readCSV))
    if not classValueFileExist:
        featureCount -= 1
    csvfile.seek(0)
    print("\nFeature count: ")
    print(featureCount)

    # Name features, if provided
    if featureNames:
        names = next(readCSV)
        if not classValueFileExist:
            names.pop()
    else:
        for x in range(featureCount):
            names.append(x)
    print("Names: ")
    print(names)

    # Populate data list
    for row in readCSV:
        rowList = []
        for x in range(featureCount):
            rowEntry = float(row[x])
            rowList.append(rowEntry)
        data.append(rowList)

    # Populate class list
    if not classValueFileExist:
        csvfile.seek(0)
        for row in readCSV:
            classValues.append(row[featureCount])

# Open class label file if applicable
if classValueFileExist:
    with open(classValueFile) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        # Populate class list
        if featureNamesExist:
            classValueName = next(readCSV)
        for row in readCSV:
            classValues.append(row[0])

print("Class label name: ")
print(classValueName)

# Append class labels to data set
entry = -1
for x in data:
    entry += 1
    classLabel = classValues[entry]
    if classLabel == 'True':
        classLabel = 1
    elif classLabel == 'False':
        classLabel = 0
    else:
        classLabel = int(classLabel)
    data[entry].append(classLabel)
