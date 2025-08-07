# Final-Project-Part-1-Optimization-Technique-and-Implementation-Project-Report
# HPC Caching Optimization - Fibonacci Example

## Overview
The purpose of this project is to demonstrate how caching, memoization, and the use of lookup tables impact optimization techniques especially in HPC. 

## Files
- **naive_recursive.py**: Naïve recursive Fibonacci uses no caching and very slow for large `n`.
- **memoized_recursive.py**: Fibonacci with Python's `functools.lru_cache` for memoization.
- **lookup_table_dp.py**: Dynamic Programming implementation using a pre-allocated lookup table.
- **benchmark.py**: Script to benchmark and compare execution times of the above methods.

## How to Run
we can run teh model through the following steps. 
1. You can clone the repository or download the files.
2. The scripts can be executed using atlest Python 3.x and above.
3. To get the reulst, we run the benchmark script as,
    ```bash
    python benchmark.py
    ```
