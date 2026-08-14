# Name: Nour
# Class: CS 325
# Homework 1
# Timing program for Stooge Sort

import random
import time
import math


def stooge_sort(arr, low, high):
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    n = high - low + 1

    if n >= 3:
        k = int(math.ceil((2.0 * n) / 3.0))

        stooge_sort(arr, low, low + k - 1)

        stooge_sort(arr, high - k + 1, high)

        stooge_sort(arr, low, low + k - 1)


sizes = [
    50,
    100,
    150,
    200,
    250,
    300,
    350,
    400,
    450,
    500
]

print("n Time(ms)")

for n in sizes:
    arr = [random.randint(0, 10000) for _ in range(n)]

    start = time.perf_counter()

    stooge_sort(arr, 0, len(arr) - 1)

    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000

    print(n, "{:.4f}".format(elapsed_ms))