from src.algorithms.sliding_window.FixedWindowConfig import FixedWindowConfig
from random import randrange
from typing import List


def create_test_config(
    cont_size: int = 100,
    width: int = 1,
) -> FixedWindowConfig:
    return FixedWindowConfig(range(cont_size), width)


def randomly_place_window_in_list(container: List, window: List[int]) -> None:
    width = len(window)
    placement_starting_index = randrange(0, len(container) - width + 1)
    for i in range(width):
        container[placement_starting_index + i] = window[i]


def create_list_with_randomly_placed_window(
    container_sz: int,
    window: List[int],
) -> List[int]:
    container = list(range(container_sz))
    randomly_place_window_in_list(container, window)
    return container
