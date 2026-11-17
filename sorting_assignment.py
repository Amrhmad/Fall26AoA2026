"""
Assignment: Empirical Analysis of Sorting Algorithms
Course: Analysis of Algorithms

Implements Selection Sort, Bubble Sort, Quick Sort, and Merge Sort
from scratch. Each algorithm is tested on four required input cases.
Each case is run three times and the average time is reported.
"""

import time
import statistics


def selection_sort(arr):
    """Sort arr in place using Selection Sort."""
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(arr):
    """Sort arr in place using optimized Bubble Sort."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(arr):
    """Return a sorted list using Quick Sort (last element as pivot)."""
    if len(arr) <= 1:
        return arr[:]

    pivot = arr[-1]
    smaller = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(greater)


def merge_sort(arr):
    """Return a sorted list using Merge Sort."""
    if len(arr) <= 1:
        return arr[:]

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


ALGORITHMS = {
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
}


def make_test_cases():
    return {
        "Size 5 - Sorted": list(range(1, 6)),
        "Size 5 - Reverse": list(range(5, 0, -1)),
        "Size 100 - Sorted": list(range(1, 101)),
        "Size 100 - Reverse": list(range(100, 0, -1)),
    }


def benchmark(sort_function, original, repetitions=3):
    """Return average elapsed time in seconds and verify correctness."""
    times = []
    for _ in range(repetitions):
        data = original.copy()  # Copy is outside the timed section.
        start = time.perf_counter()
        result = sort_function(data)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

        # In-place algorithms return data; recursive algorithms return a list.
        if result != sorted(original):
            raise AssertionError("Sorting algorithm produced an incorrect result.")

    return statistics.mean(times)


def main():
    cases = make_test_cases()
    print("Average execution time (seconds), based on 3 runs")
    print("-" * 75)

    for algorithm_name, sort_function in ALGORITHMS.items():
        print(f"\\n{algorithm_name}")
        for case_name, values in cases.items():
            average = benchmark(sort_function, values)
            print(f"{case_name:24s}: {average:.10f} seconds")


if __name__ == "__main__":
    main()
