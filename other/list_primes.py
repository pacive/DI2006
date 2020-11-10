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

