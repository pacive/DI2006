# Calculates the factorial of num
def factorial(num):
    product = 1
    for n in range(2, num + 1):
        product *= n
    return product

number = int(input('Skriv ett tal: '))

print(f'{number}! = {factorial(number)}')
        