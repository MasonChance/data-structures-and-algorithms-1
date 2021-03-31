import pytest
from code_challenges.insert_sort import insert_sort

def test_insert_sort_base():
    unsorted = [8, 4, 23, 42, 16, 15]
    actual = insert_sort(unsorted)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected 

def test_insert_sort_reverse_input():
    pass

def test_insert_sort_few_unique():
    pass

def test_insert_sort_nearly_sorted():
    pass


