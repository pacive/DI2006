# Calculates an approximation of pi using a mathematical formula.
# More iterations make the result more accurate
def pi(iterations):
    sum = 0
    for n in range(0, iterations):
        rational = ((-1) ** n) / (2 * n + 1)
        sum += rational
    return sum * 4

number = int(input('Hur många iterationer? '))

print(pi(number))