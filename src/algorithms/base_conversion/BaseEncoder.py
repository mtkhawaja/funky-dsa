from __future__ import annotations
from collections import deque
from src.algorithms.base_conversion.AlphabetGenerator import AlphabetGenerator


class BaseEncoder:

    @classmethod
    def encode(cls: BaseEncoder,
               b10_int: int, base: int, alphabet: str = "") -> str:
        if not alphabet:
            alphabet = AlphabetGenerator.generate_alphabet_from_base(base)
        return cls.int_to_base(b10_int, base, alphabet)

    @staticmethod
    def int_to_base(b10_int: int, base: int, alphabet: str) -> str:
        if not b10_int:
            return "0"
        target_base_digits = deque()
        while b10_int:
            remainder = b10_int % base
            target_base_digits.appendleft(alphabet[remainder])
            b10_int //= base
        return "".join(target_base_digits)
