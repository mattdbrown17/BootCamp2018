# IntroMatplotlib.py
import numpy as np
import matplotlib.pyplot as plt
# Exercise 1
def ex1func(n):
    '''
    This function accepts an integer n, creates an nxn matrix of samples
    from the normal distribution with mean 0, st. dev. 1, computes the
    mean of each row of the matrix, and computes the variance of these
    means.
    '''
    matrix = np.random.normal(size=(n, n))
    means = np.sum(matrix, axis = 1) / n
    var = np.var(means)
    return var

def ex1func2():
    '''
    This function creates an array of the integers, 100, 200, ..., 1000
    and the corresponding outputs of ex1func().
    '''
    array = zeroes(2, 10)
    array[0] = np.linspace(100, 1000, num = 10)
    array[1] = ex1func(array[0])
