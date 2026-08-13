# Name: Nour
# Class: CS 325
# Homework 1
# Stooge Sort implementation

import math


def stooge_sort(arr, low, high):
    # Swap first and last values if needed
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    n = high - low + 1

    if n >= 3:
        # Round 2/3 upward
        k = math.ceil((2 * n) / 3)

        # Sort first 2/3
        stooge_sort(arr, low, low + k - 1)

        # Sort last 2/3
        stooge_sort(arr, high - k + 1, high)

        # Sort first 2/3 again
        stooge_sort(arr, low, low + k - 1)


def main():
    with open("hw1-data.txt", "r") as file:
        for line in file:
            values = list(map(int, line.split()))

            if not values:
                continue

            n = values[0]
            arr = values[1:n + 1]

            if len(arr) > 0:
                stooge_sort(arr, 0, len(arr) - 1)

            print(" ".join(map(str, arr)))


if __name__ == "__main__":
    main()
