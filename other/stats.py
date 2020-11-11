import math

def mean(array):
    return sum(array) / len(array)

def variance(array):
    m = mean(array)
    diffs = [(n - m) ** 2 for n in array]
    return mean(diffs)

def stddev(array):
    return math.sqrt(variance(array))

arr = [5, 6, 9, 7, 5, 4, 6, 7, 2, 4]
print(sum(arr))
print(mean(arr))
print(stddev(arr))