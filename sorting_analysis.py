import time
import statistics
import csv
import matplotlib.pyplot as plt

def bubble_sort(a):
    a = a.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def selection_sort(a):
    a = a.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(a):
    a = a.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(a):
    if len(a) <= 1:
        return a.copy()
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
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

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
}

def main():
    sizes = [5, 10, 50, 100]
    results = {name: {} for name in algorithms}

    for n in sizes:
        # Descending order is used as a worst-case input for the O(n^2) algorithms.
        data = list(range(n, 0, -1))
        repetitions = max(20, min(2000, 200000 // (n * n)))

        for name, algorithm in algorithms.items():
            run_averages = []
            for _ in range(5):  # At least five runs per input size
                start = time.perf_counter_ns()
                for _ in range(repetitions):
                    algorithm(data)
                elapsed = time.perf_counter_ns() - start
                run_averages.append(elapsed / repetitions / 1_000_000)
            results[name][n] = statistics.mean(run_averages)
            print(f"{name:15} N={n:3}: {results[name][n]:.8f} ms")

    with open("sorting_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Algorithm", "Input Size (N)", "Average Time (ms)"])
        for name in algorithms:
            for n in sizes:
                writer.writerow([name, n, results[name][n]])

    for name in algorithms:
        plt.plot(sizes, [results[name][n] for n in sizes], marker="o", label=name)
    plt.xlabel("Input size (N)")
    plt.ylabel("Average execution time (milliseconds)")
    plt.title("Empirical Analysis of Sorting Algorithms")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("sorting_comparison.png", dpi=200)
    plt.show()

if __name__ == "__main__":
    main()
