import pytest
import two_sum as ts


def test_two_sum_error_too_many():
    lst = [0 for i in range(105)]
    with pytest.raises(ValueError):
        ts.two_sum(lst, 1)


def test_two_sum_error_too_few():
    lst = []
    with pytest.raises(ValueError):
        ts.two_sum(lst, 1)


def test_two_sum_error_too_small():
    lst = [1, 2, 3]
    target = -110
    with pytest.raises(ValueError):
        ts.two_sum(lst, target)


def test_two_sum_error_too_big():
    lst = [1, 2, 3]
    target = 110
    with pytest.raises(ValueError):
        ts.two_sum(lst, target)


def test_should_pass():
    nums, target = [2, 7, 11, 15], 9
    assert [0, 1] == ts.two_sum(nums, target) or [1, 0] == ts.two_sum(nums, target)


def test_should_pass2():
    nums, target = [3, 3], 6
    assert [0, 1] == ts.two_sum(nums, target) or [1, 0] == ts.two_sum(nums, target)


def test_should_pass3():
    nums, target = [3, 2, 4], 6
    assert [2, 1] == ts.two_sum(nums, target) or [1, 2] == ts.two_sum(nums, target)
