import math

def list_primes_upto(max, initial = [2, 3, 5, 7]):
    if max <= initial[-1]:
        return initial

    for i in range(initial[-1] + 2, max + 1, 2):
        root = int(math.sqrt(i))
        p = True
        for prime in initial:
            if prime > root:
                break
            if i % prime == 0:
                p = False
                break
        if p:
            initial.append(i)
    
    return initial

def largest_prime(limit):
    if limit % 2 == 0:
        limit -= 1

    for i in range(limit, 2, -2):
        root = int(math.sqrt(i))
        is_prime = True
        for n in range(3, root + 1, 2):
            if i % n == 0:
                is_prime = False
                break

        if is_prime:
            return i
