from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"
    number = 1000

    # Execute the code 'number' different times and return the time in seconds that each iterative execution took
    cumulative_times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=number)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(cumulative_times) / number}s")