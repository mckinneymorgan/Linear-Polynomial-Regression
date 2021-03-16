# Original author: Morgan McKinney 3/2021

import math
import numpy

def preprocess():

def get_h_theta(m, x):
    # Reference: https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
    transposed_theta = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    h_theta = transposed_theta * x
    return h_theta

def weight_update():
    # Calculate h_theta(x) = theta^T * x
    # Calculate raw error