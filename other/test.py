import sys
import os
import time
import importlib
import stats
sys.path.append(os.path.abspath('./DI2006'))
prime = importlib.import_module('11_as2.prime')

def test(func, iterations, *args):
    timings = []
    for _ in range(iterations):
        start = time.perf_counter_ns()
        func(*args)
        timings.append(time.perf_counter_ns() - start)

    print(f'''
    {func} called {iterations} times
    Total:\t{sum(timings):>10} ns
    Mean:\t{stats.mean(timings):>10.2f} ns
    Stddev:\t{stats.stddev(timings):>10.2f} ns
    ''')

test(prime.is_prime, 1000, 9999991)
