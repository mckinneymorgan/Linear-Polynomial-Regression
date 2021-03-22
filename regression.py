# Original author: Morgan McKinney 3/2021

import math
import numpy


def preprocess(data):
    for x in data:
        x_i = (x_i - min(x)) / (max(x) - min(x))
    return x_i


def get_h_theta(m, x):
    # Reference: https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
    transposed_theta = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    h_theta = transposed_theta * x
    return h_theta


def get_raw_error():
    return 0


def get_gradient():
    return 0


def weight_update(d, alpha):
    # Calculate h_theta(x) = theta^T * x
    h_theta = get_h_theta()
    # Calculate raw error e = h_theta(x) - y
    raw_error = get_raw_error()
    # Calculate gradient = e * x
    gradient = get_gradient()
    # Perform update using scalar operations
    theta = theta_old - alpha * gradient
    return 0
