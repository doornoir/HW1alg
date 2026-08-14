# Name: Nour
# Class: CS 325
# Homework 1
# Timing program for Mergesort3

import random
import time


def merge3(left, middle, right):
    result = []

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(middle) and k < len(right):
        if left[i] <= middle[j] and left[i] <= right[k]:
            result.append(left[i])
            i += 1
        elif middle[j] <= left[i] and middle[j] <= right[k]:
            result.append(middle[j])
            j += 1
        else:
            result.append(right[k])
            k += 1

    while i < len(left) and j < len(middle):
        if left[i] <= middle[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(middle[j])
            j += 1

    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[k])
            k += 1

    while j < len(middle) and k < len(right):
        if middle[j] <= right[k]:
            result.append(middle[j])
            j += 1
        else:
            result.append(right[k])
            k += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(middle):
        result.append(middle[j])
        j += 1

    while k < len(right):
        result.append(right[k])
        k += 1

    return result


def mergesort3(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr)

    first_split = n // 3
    second_split = (2 * n) // 3

    left = arr[:first_split]
    middle = arr[first_split:second_split]
    right = arr[second_split:]

    if len(left) == 0:
        left = [middle.pop(0)]

    left = mergesort3(left)
    middle = mergesort3(middle)
    right = mergesort3(right)

    return merge3(left, middle, right)


sizes = [
    5000,
    10000,
    15000,
    20000,
    25000,
    30000,
    35000,
    40000,
    45000,
    50000
]

print("n Time(ms)")

for n in sizes:
    arr = [random.randint(0, 10000) for _ in range(n)]

    start = time.perf_counter()

    mergesort3(arr)

    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000

    print(n, "{:.4f}".format(elapsed_ms))