# Name: Nour
# Class: CS 325
# Homework 1
# Mergesort3 implementation

def merge3(left, middle, right):
    result = []

    i = 0
    j = 0
    k = 0

    # Compare all three lists while all still have values
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

    # Merge left and middle if right is empty
    while i < len(left) and j < len(middle):
        if left[i] <= middle[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(middle[j])
            j += 1

    # Merge left and right if middle is empty
    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[k])
            k += 1

    # Merge middle and right if left is empty
    while j < len(middle) and k < len(right):
        if middle[j] <= right[k]:
            result.append(middle[j])
            j += 1
        else:
            result.append(right[k])
            k += 1

    # Add anything remaining
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

    # Split into three parts
    first_split = n // 3
    second_split = (2 * n) // 3

    left = arr[:first_split]
    middle = arr[first_split:second_split]
    right = arr[second_split:]

    # Edge case for very small arrays
    if len(left) == 0:
        left = [middle.pop(0)]

    left = mergesort3(left)
    middle = mergesort3(middle)
    right = mergesort3(right)

    return merge3(left, middle, right)


def main():
    with open("hw1-data.txt", "r") as file:
        for line in file:
            values = list(map(int, line.split()))

            if not values:
                continue

            n = values[0]
            arr = values[1:n + 1]

            sorted_arr = mergesort3(arr)

            print(" ".join(map(str, sorted_arr)))


if __name__ == "__main__":
    main()
