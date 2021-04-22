from __future__ import annotations
from typing import Callable, Iterable, List
import src.algorithms.sliding_window.util as sw_util


class FixedWindowConfig:
    def __init__(
        self,
        container: Iterable,
        window_width: int,
        operation: Callable = sw_util.addition,
        inverse_operation: Callable = sw_util.subtraction,
        comparator: Callable = sw_util.max_integer_comparator,
    ) -> None:
        self.container = container
        self.window_width = window_width
        self.operation = operation
        self.inverse_operation = inverse_operation
        self.comparator = comparator

    @staticmethod
    def max_sum_config(container: List[int], width: int) -> FixedWindowConfig:
        return FixedWindowConfig(
            container,
            width,
            operation=sw_util.addition,
            inverse_operation=sw_util.subtraction,
            comparator=sw_util.max_integer_comparator,
        )

    @staticmethod
    def min_sum_config(container: List[int], width: int) -> FixedWindowConfig:
        return FixedWindowConfig(
            container,
            width,
            operation=sw_util.addition,
            inverse_operation=sw_util.subtraction,
            comparator=sw_util.min_integer_comparator,
        )

    @staticmethod
    def max_product_config(
        container: List[int],
        width: int,
    ) -> FixedWindowConfig:
        return FixedWindowConfig(
            container,
            width,
            operation=sw_util.integer_multiplication,
            inverse_operation=sw_util.integer_division,
            comparator=sw_util.max_integer_comparator,
        )

    @staticmethod
    def min_product_config(
        container: List[int],
        width: int,
    ) -> FixedWindowConfig:
        return FixedWindowConfig(
            container,
            width,
            operation=sw_util.integer_multiplication,
            inverse_operation=sw_util.integer_division,
            comparator=sw_util.min_integer_comparator,
        )

    def __str__(self) -> str:
        attrs = vars(self)
        attrs["container_size"] = len(self.container)
        return str(attrs)