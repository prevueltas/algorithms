from random import randint

from performance import run_sorting_algorithm


def quicksort(arr: []) -> []:
    if len(arr) < 2:
        return arr
    else:
        # Randomly selecting the pivot makes the worst case very unlikely
        pivot = arr[randint(0, len(arr) - 1)]
        less, same, greater = [], [], []

        for item in arr:
            if item < pivot:
                less.append(item)
            elif item > pivot:
                greater.append(item)
            else:
                same.append(item)

        return quicksort(less) + same + quicksort(greater)


if __name__ == "__main__":
    array = [randint(-1000, 1000) for i in range(10000)]
    run_sorting_algorithm(algorithm="quicksort", array=array)
