# Calculates the factorial of num
def factorial(num):
    product = 1
    for i in range(2, num + 1):
        product *= i
    return product

number = int(input('Skriv ett tal: '))

print('{}! = {}'.format(number, factorial(number)))
        