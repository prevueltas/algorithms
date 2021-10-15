from random import randint

from performance import run_sorting_algorithm


def find_smallest(arr: []) -> int:
    smallest = arr[0]
    index = 0

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i

    return index


def selection_sort(arr: []) -> []:
    sorted_array = []

    for i in range(len(arr)):
        index = find_smallest(arr)
        sorted_array.append(arr.pop(index))

    return sorted_array


if __name__ == "__main__":
    array = [randint(-1000, 1000) for i in range(1000)]
    run_sorting_algorithm(algorithm="selection_sort", array=array)
