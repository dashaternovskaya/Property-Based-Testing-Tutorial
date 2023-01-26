from hypothesis import given, strategies as st
from collections import Counter


# The wrong sorting function (that does not sort lists of integers) to test property completeness
def my_sort(lst):
    if not lst:
        return []

    s = sorted(set(lst))
    return s + [s[-1]] * (len(lst) - len(s))


"""
The function my_sort must have the following properties:
    1) the input and the output should have the same length;
    2) the result should only contain numbers from the original list;
    3) the result must be actually sorted.
"""
@given(st.lists(st.integers()))  # 'lists' - a strategy to generate lists
def test_my_sort(int_list):
    result = my_sort(int_list)

    assert len(result) == len(int_list)  # 1) The input and the output should have the same length

    # 2) The result should only contain numbers from the original list and it must be
    #    taken into account how many times each number appears in the original list
    assert Counter(result) == Counter(int_list)

    # 3) The result must be actually sorted
    for a, b in zip(result, result[1:]):
        assert a <= b


"""
To help mitigate the danger of having come up with an insufficient set of properties,
it is perfectly reasonable to mix property-based testing with other forms of testing.

For example, on top of having the property-based test test_my_sort, the following test could be added:
"""
def test_my_sort_specific_examples():
    assert my_sort([]) == []
    assert my_sort(list(range(10)[::-1])) == list(range(10))
    assert my_sort([42, 73, 0, 16, 10]) == [0, 10, 16, 42, 73]
