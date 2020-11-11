import math

def mean(array):
    return sum(array) / len(array)

def variance(array):
    m = mean(array)
    diffs = [(n - m) ** 2 for n in array]
    return mean(diffs)

def stddev(array):
    return math.sqrt(variance(array))
