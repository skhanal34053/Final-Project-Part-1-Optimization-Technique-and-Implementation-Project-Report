# lookup_table_dp.py

def dp_fibonacci(n):
    if n <= 1:
        return n
    lookup = [0] * (n + 1)
    lookup[1] = 1

    for i in range(2, n + 1):
        lookup[i] = lookup[i - 1] + lookup[i - 2]
    return lookup[n]

if __name__ == "__main__":
    n = 1000
    print(f"DP Lookup Table Fibonacci({n}) = {dp_fibonacci(n)}")
