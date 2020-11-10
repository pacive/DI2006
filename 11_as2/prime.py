import math

def is_prime(num):
    # Only need to test factors up to the sqare root of num
    largest_factor = int(math.sqrt(num)) + 1

    # Check if num is 2 or else a multiple of 2, since it's the only even prime
    if num == 2:
        return True
    elif num % 2 == 0:
        return False

    # Then only odd factors need to be checked
    for i in range(3, largest_factor, 2):
        if num % i == 0:
            return False
    
    # If not divisible by any number, it must be a prime
    return True

number = int(input('Skriv ett tal: '))

if is_prime(number):
    print(f'{number} är ett primtal')
else:
    print(f'{number} är inte ett primtal')
