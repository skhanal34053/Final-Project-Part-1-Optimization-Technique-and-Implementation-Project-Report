# benchmark.py

import time
from naive_recursive import naive_fibonacci
from memoized_recursive import memoized_fibonacci
from lookup_table_dp import dp_fibonacci

def benchmark(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    print(f"{func.__name__}({n}) = {result} | Time taken: {end - start:.6f} seconds")

if __name__ == "__main__":
    n_naive = 35  # Naive recursive is too slow beyond 35
    n_memo = 1000
    n_dp = 1000

    print("Benchmarking Naive Recursive (O(2^n))")
    benchmark(naive_fibonacci, n_naive)

    print("\nBenchmarking Memoized Recursive (O(n))")
    benchmark(memoized_fibonacci, n_memo)

    print("\nBenchmarking DP Lookup Table (O(n))")
    benchmark(dp_fibonacci, n_dp)
