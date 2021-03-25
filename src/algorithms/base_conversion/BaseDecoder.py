from __future__ import annotations
from typing import List, Dict
from src.algorithms.base_conversion.AlphabetGenerator import AlphabetGenerator as AG  # noqa: E501


class BaseDecoder:

    @classmethod
    def decode(cls: BaseDecoder, key_str: str, base: int,
               alphabet_map: Dict[str, int] = None) -> int:
        if not alphabet_map:
            alphabet_map = AG.generate_alphabet_map_from_base(base)
        return cls.encoded_str_to_base_10_int(key_str, base, alphabet_map)

    @classmethod
    def encoded_str_to_base_10_int(cls: BaseDecoder, encoded_str: str,
                                   base: int, alphabet_map: dict) -> int:
        tokens = cls.tokenize(encoded_str, alphabet_map)
        base_10_num = 0
        for index, digit_place in enumerate(range(len(tokens)-1, -1, -1)):
            base_10_num += cls.process_token(digit_place,
                                             alphabet_map[tokens[index]],
                                             base)
        return base_10_num

    @staticmethod
    def tokenize(encoded_str: str, alphabet_map: Dict[str, int]) -> List[str]:
        digit, tokens = "", []
        for symbol in encoded_str:
            digit += symbol
            if digit in alphabet_map:
                tokens.append(digit)
                digit = ""
        return tokens

    @staticmethod
    def process_token(digit_place: int, digit_val: int, base: int) -> int:
        return digit_val * (base ** digit_place)
