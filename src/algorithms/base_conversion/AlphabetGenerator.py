from __future__ import annotations
from string import ascii_letters, digits
from typing import List, Dict


class AlphabetGenerator:

    @classmethod
    def generate_alphabet_from_base(cls: AlphabetGenerator, base: int,
                                    char_set: str = "") -> List[str]:
        if base <= 0:
            raise ValueError('Error: Base must be >= 1 !')
        char_set = cls.default_char_set() if not char_set else char_set
        alphabet = cls._generate_base_alphabet(base, char_set)
        if cls._needs_extension(base, char_set):
            alphabet += cls._generate_extended_alphabet(base, alphabet)
        return alphabet

    @classmethod
    def default_char_set(cls) -> List[str]:
        return "".join([digits, ascii_letters])

    @classmethod
    def _generate_base_alphabet(cls, base: int, char_set: str) -> List[str]:
        return [char_set[i] for i in range(min(base, len(char_set)))]

    @classmethod
    def _needs_extension(cls, base: int, char_set: str) -> bool:
        return base > len(char_set)

    @classmethod
    def _generate_extended_alphabet(cls, base: int, char_set: str = "",
                                    prefix_char: str = '~') -> List[str]:
        char_limit, extension = len(char_set), base - len(char_set)
        prefix, extended_alphabet = "", []
        for out_of_bounds_index in range(extension):
            index = out_of_bounds_index % char_limit
            prefix = prefix if index else (prefix + prefix_char)
            extended_alphabet.append(prefix + char_set[index])
        return extended_alphabet

    @classmethod
    def generate_alphabet_map_from_base(cls: AlphabetGenerator,
                                        base: int) -> Dict[str, int]:
        alphabet = cls.generate_alphabet_from_base(base)
        return dict(zip(alphabet, range(base)))
