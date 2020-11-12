# Calculates an approximation of pi using a mathematical formula.
# More iterations make the result more accurate
def calculate_pi(iterations):
    total = 0
    for n in range(0, iterations):
        rational = ((-1) ** n) / (2 * n + 1)
        total += rational
    return total * 4

number = int(input('Hur många iterationer? '))

print(calculate_pi(number))
