from typing import Callable
from functools import wraps


def argument_validator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args):
        if args[1].window_width < 0:
            raise ValueError(
                f"Error: Window width must be a non-negative integer!\n{args[1]}"
            )
        if args[1].window_width > len(args[1].container):
            raise ValueError(
                f"Window width must be a less than or equal to container size\n{args[1]}"
            )
        return func(*args)

    return wrapper
