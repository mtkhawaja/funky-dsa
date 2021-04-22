from __future__ import annotations
from typing import Any, Iterator
from src.algorithms.sliding_window.FixedWindowConfig import FixedWindowConfig
from src.algorithms.sliding_window.Validators import argument_validator


class FixedWidthSlidingWindow:
    @classmethod
    @argument_validator
    def slide(cls: FixedWidthSlidingWindow, config: FixedWindowConfig) -> Any:
        best_result = running_result = cls._starting_window(config)
        back_itr = iter(config.container)
        for element in cls._forward_iterator(config):
            running_result = config.operation(running_result, element)
            running_result = config.inverse_operation(
                running_result,
                next(back_itr),
            )
            if config.comparator(running_result, best_result) > 0:
                best_result = running_result
        return best_result

    @staticmethod
    def _starting_window(config: FixedWindowConfig) -> Any:
        initial_window = config.container[0]
        for i in range(1, config.window_width):
            initial_window = config.operation(
                initial_window,
                config.container[i],
            )
        return initial_window

    @staticmethod
    def _forward_iterator(config: FixedWindowConfig) -> Iterator:
        iterator = iter(config.container)
        [next(iterator) for _ in range(config.window_width)]
        return iterator
    
