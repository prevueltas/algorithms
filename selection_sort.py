# Selection Sort - O(n^2)

import random
from array import array
from datetime import datetime


def find_smallest(arr: array) -> int:
    smallest = arr[0]
    index = 0

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i

    return index


def selection_sort(arr: array) -> array:
    sorted_array = array('i')

    for i in range(len(arr)):
        index = find_smallest(arr)
        sorted_array.append(arr.pop(index))

    return sorted_array


array_to_sort = array('i', random.sample(range(-10**6, 10**6), 10**4))

start_time = datetime.now()
arr = selection_sort(array_to_sort)
end_time = datetime.now()

print(arr[:5], arr[-5:])
print(f"Duration: {format(end_time - start_time)}")
