# naive_recursive.py

def naive_fibonacci(n):
    if n <= 1:
        return n
    return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)

if __name__ == "__main__":
    n = 35  # Warning: Higher values will be VERY slow!
    print(f"Naive Recursive Fibonacci({n}) = {naive_fibonacci(n)}")
