# Original author: Morgan McKinney 3/2021

import math
import numpy


def preprocess(data):
    for x in data:
        x_i = (x_i - min(x)) / (max(x) - min(x))
    return x_i

