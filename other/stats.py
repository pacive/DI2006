import math

def sum(array):
    sum = 0
    for n in array:
        sum += n
    return sum

def mean(array):
    return sum(array) / len(array)

def variance(array):
    m = mean(array)
    diffs = []
    for n in array:
        diffs.append((n - m) ** 2)
    return mean(diffs)

def stddev(array):
    return math.sqrt(variance(array))
