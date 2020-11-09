import math

def is_prime(num):
    # Only need to test numbers up to the sqare root of num
    largest_factor = int(math.sqrt(num)) + 1

    # Check if divisible by 2, since it's the only even prime
    if num % 2 == 0:
        return False

    # Then only odd numbers need to be checked
    for i in range(3, largest_factor, 2):
        if num % i == 0:
            return False
    
    # If not divisible by any number, it must be a prime
    return True

number = int(input('Skriv ett tal: '))

if is_prime(number):
    print('{} är ett primtal'.format(number))
else:
    print('{} är inte ett primtal'.format(number))
