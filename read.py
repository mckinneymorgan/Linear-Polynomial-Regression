# Original author: Morgan McKinney 3/2021

import csv
import sys


def read_file(names, classValueName, data, classValues):
    class_value_file_exist = False
    feature_names = False

    # User input, get filename(s)
    file = input("Enter csv file name: ")
    class_value_file = input("Are the class labels in another file (Y/N): ")
    if class_value_file.lower() == 'y':
        class_value_file = input("Enter class label file name: ")
        class_value_file_exist = True
    elif class_value_file.lower() != 'n':
        sys.exit("Invalid input")
    feature_names_exist = input("Are the features named (Y/N): ")
    if feature_names_exist.lower() == 'y':
        feature_names = True
    elif feature_names_exist.lower() != 'n':
        sys.exit("Invalid input")

    # Read file
    with open(file) as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')

        # Count features, return to start of file
        feature_count = len(next(read_csv))
        if not class_value_file_exist:
            feature_count -= 1
        csvfile.seek(0)
        print("\nFeature count: ")
        print(feature_count)

        # Name features, if provided
        if feature_names:
            names = next(read_csv)
            if not class_value_file_exist:
                names.pop()
        else:
            for x in range(feature_count):
                names.append(x)
        print("Names: ")
        print(names)

        # Populate data list
        for row in read_csv:
            row_list = []
            for x in range(feature_count):
                row_entry = float(row[x])
                row_list.append(row_entry)
            data.append(row_list)

        # Populate class list
        if not class_value_file_exist:
            csvfile.seek(0)
            for row in read_csv:
                classValues.append(row[feature_count])

    # Open class label file if applicable
    if class_value_file_exist:
        with open(class_value_file) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')

            # Populate class list
            if feature_names_exist:
                classValueName = next(read_csv)
            for row in read_csv:
                classValues.append(row[0])

    print("Class label name: ")
    print(classValueName)

    # Append class labels to data set
    entry = -1
    for x in data:
        entry += 1
        class_label = classValues[entry]
        if class_label == 'True':
            class_label = 1
        elif class_label == 'False':
            class_label = 0
        else:
            class_label = float(class_label)
        data[entry].append(class_label)
