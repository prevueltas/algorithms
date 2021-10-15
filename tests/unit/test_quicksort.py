import random
import pytest

from quicksort import quicksort

a = [random.randint(-100, 100) for i in range(10000)]


@pytest.mark.parametrize("input_list, output_list", [
    ([2], [2]),
    ([2, 3], [2, 3]),
    ([3, 2], [2, 3]),
    ([3, 1, 5], [1, 3, 5]),
    (a, sorted(a)),
])
def test_quicksort_order_a_list(input_list, output_list):
    assert quicksort(input_list) == output_list
