from __future__ import annotations
from random import randint
from typing import Any
import importlib


class Roulette:

    candidates = [('builtins', 'list'), ('builtins', 'dict'),
                  ('builtins', 'set'), ('builtins', 'tuple'),
                  ('collections', 'deque'), ('collections', 'Counter')]

    @classmethod
    def roll(cls: Roulette) -> object:
        module, class_name = cls.candidates[cls.random_valid_index()]
        return cls.create_object(module, class_name)

    @classmethod
    def random_valid_index(cls: Roulette) -> int:
        return randint(0, len(cls.candidates)-1)

    @classmethod
    def create_object(cls: Roulette, module_name: str, class_name: str) -> Any:
        module = importlib.import_module(module_name)
        class_ptr = getattr(module, class_name)
        return class_ptr()
