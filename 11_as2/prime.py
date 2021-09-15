import math
import sys

def prime_factors(num, start = 3):
    # Check if num is 2 - the only even prime
    if num == 2:
        return [2]

    # If num is even, it can't be a prime
    if num % 2 == 0:
        return [2] + prime_factors(num // 2)

    # Only need to test factors up to the sqare root of num
    largest_factor = int(math.sqrt(num))

    # If num is divisible by any other number, it's not prime
    for n in range(start, largest_factor + 1, 2):
        if num % n == 0:
            return [n] + prime_factors(num // n, n)

    # If not divisible by any number, it must be a prime
    return [num]

if not (len(sys.argv) > 1 and (number := int(sys.argv[1]))):
    number = int(input('Skriv ett tal: '))

factors = prime_factors(number)

if len(factors) == 1:
    print(f'{number} är ett primtal')
else:
    print(f'{number} faktoriseras till {factors}')