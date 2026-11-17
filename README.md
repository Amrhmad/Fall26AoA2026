# Empirical Analysis of Sorting Algorithms

## Contents
- `sorting_analysis.py`: Python implementation and benchmark for Bubble, Selection, Insertion, and Merge Sort.
- `sorting_results.csv`: measured average execution times.
- `sorting_comparison.png`: comparison graph.
- `SAP_Name_SortingAnalysis.pdf`: assignment report.

## Requirements
Python 3.9 or later and matplotlib.

Install matplotlib:
```bash
python -m pip install matplotlib
```

Run:
```bash
python sorting_analysis.py
```

The program tests input sizes N = 5, 10, 50, and 100. It uses descending arrays as worst-case-style input for the quadratic algorithms, performs five measurement runs per size, averages the results, writes a CSV file, and saves a graph.

Execution times depend on the computer and Python environment. Run the script on your own computer if you need measurements from your own device.
