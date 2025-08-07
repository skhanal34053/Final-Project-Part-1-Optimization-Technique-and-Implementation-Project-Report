# memoized_recursive.py

from functools import lru_cache

@lru_cache(maxsize=None)
def memoized_fibonacci(n):
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

if __name__ == "__main__":
    n = 1000  # Can handle very large n efficiently now
    print(f"Memoized Recursive Fibonacci({n}) = {memoized_fibonacci(n)}")
