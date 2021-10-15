import random
import pytest

from algorithms.quicksort import quicksort

a = [random.randint(-100, 100) for i in range(10000)]


@pytest.mark.parametrize("input_list, output_list", [
    ([2], [2]),
    ([2, 3], [2, 3]),
    ([3, 2], [2, 3]),
    ([3, 1, 5], [1, 3, 5]),
    (a, sorted(a)),
])
class TestSortingAlgorithms:

    def test_selection_sort(self, input_list, output_list):
        assert quicksort(input_list) == output_list

    def test_quicksort(self, input_list, output_list):
        assert quicksort(input_list) == output_list
