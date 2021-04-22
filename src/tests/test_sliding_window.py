import src.tests.util.sliding_window as sw_test
from pytest import raises
from src.algorithms.sliding_window.FixedWidthSlidingWindow import (
    FixedWidthSlidingWindow as FWSW,
)
from src.algorithms.sliding_window.FixedWindowConfig import FixedWindowConfig


def test_for_value_exception_when_width_is_negative():
    config = sw_test.create_test_config(width=-1)
    print(config)
    with raises(ValueError):
        assert FWSW.slide(config)


def test_for_value_exception_when_width_is_greater_than_list_size():
    config = sw_test.create_test_config(cont_size=10, width=11)
    with raises(ValueError):
        assert FWSW.slide(config)


def test_list_based_max_sum_sliding_window_of_width_zero():
    config = sw_test.create_test_config(width=0)
    assert FWSW.slide(config) == 0


def test_list_based_max_sum_sliding_window_where_width_equals_list_size():
    size = 200000
    config = sw_test.create_test_config(cont_size=size, width=size)
    assert FWSW.slide(config) == sum(range(size))


def test_list_based_max_sum_sliding_window_of_width_three():
    window = [999, 999, 999]
    numbers = sw_test.create_list_with_randomly_placed_window(1000, window)
    config = FixedWindowConfig.max_sum_config(numbers, len(window))
    assert FWSW.slide(config) == 2997


def test_list_based_min_sum_sliding_window_of_width_three():
    window = [-1, -1, -1]
    numbers = sw_test.create_list_with_randomly_placed_window(1000, window)
    config = FixedWindowConfig.min_sum_config(numbers, len(window))
    assert FWSW.slide(config) == -3


def test_list_based_max_product_sliding_window_of_width_three():
    window = [999, 999, 999]
    numbers = list(range(1, 1000, 1))
    sw_test.randomly_place_window_in_list(numbers, window)
    config = FixedWindowConfig.max_product_config(numbers, len(window))
    assert FWSW.slide(config) == 999 ** 3


def test_list_based_min_product_sliding_window_of_width_three():
    window = [-1, 9999, 9999]
    numbers = list(range(1, 1000, 1))
    sw_test.randomly_place_window_in_list(numbers, window)
    config = FixedWindowConfig.min_product_config(numbers, len(window))
    assert FWSW.slide(config) == -1 * 9999 * 9999