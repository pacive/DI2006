import math

def list_primes_upto(limit):
    initial = [2, 3, 5, 7, 11, 13]
    if limit <= initial[-1]:
        return initial

    for i in range(initial[-1] + 2, limit + 1, 2):
        root = int(math.sqrt(i))
        prime = True
        for prime_number in initial:
            if prime_number > root:
                break
            if i % prime_number == 0:
                prime = False
                break
        if prime:
            initial.append(i)

    return initial

def largest_prime(limit):
    if limit % 2 == 0:
        limit -= 1

    for i in range(limit, 2, -2):
        root = int(math.sqrt(i))
        is_prime = True
        for j in range(3, root + 1, 2):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            return i

    return 2
