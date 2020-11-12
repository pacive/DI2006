import math

def is_prime(num):
    # Only need to test factors up to the sqare root of num
    largest_factor = int(math.sqrt(num)) + 1

    # Check if num is 2 - the only even prime
    if num == 2:
        return True

    # If num is even, it can't be a prime
    if num % 2 == 0:
        return False

    # If num is divisible by any other number, it's not prime
    for n in range(3, largest_factor, 2):
        if num % n == 0:
            return False

    # If not divisible by any number, it must be a prime
    return True

number = int(input('Skriv ett tal: '))

if is_prime(number):
    print(f'{number} är ett primtal')
else:
    print(f'{number} är inte ett primtal')
