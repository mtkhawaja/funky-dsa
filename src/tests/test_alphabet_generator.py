from src.algorithms.base_conversion.AlphabetGenerator import AlphabetGenerator as AG  # noqa: E501
import pytest

base_200_chars_with_defaults = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '~0', '~1', '~2', '~3', '~4', '~5', '~6', '~7', '~8', '~9', '~a', '~b', '~c', '~d', '~e', '~f', '~g', '~h', '~i', '~j', '~k', '~l', '~m', '~n', '~o', '~p', '~q', '~r', '~s', '~t', '~u', '~v', '~w', '~x', '~y', '~z', '~A', '~B', '~C', '~D', '~E', '~F', '~G', '~H', '~I', '~J', '~K', '~L',
                                '~M', '~N', '~O', '~P', '~Q', '~R', '~S', '~T', '~U', '~V', '~W', '~X', '~Y', '~Z', '~~0', '~~1', '~~2', '~~3', '~~4', '~~5', '~~6', '~~7', '~~8', '~~9', '~~a', '~~b', '~~c', '~~d', '~~e', '~~f', '~~g', '~~h', '~~i', '~~j', '~~k', '~~l', '~~m', '~~n', '~~o', '~~p', '~~q', '~~r', '~~s', '~~t', '~~u', '~~v', '~~w', '~~x', '~~y', '~~z', '~~A', '~~B', '~~C', '~~D', '~~E', '~~F', '~~G', '~~H', '~~I', '~~J', '~~K', '~~L', '~~M', '~~N', '~~O', '~~P', '~~Q', '~~R', '~~S', '~~T', '~~U', '~~V', '~~W', '~~X', '~~Y', '~~Z', '~~~0', '~~~1', '~~~2', '~~~3', '~~~4', '~~~5', '~~~6', '~~~7', '~~~8', '~~~9', '~~~a', '~~~b', '~~~c', '~~~d']  # noqa: E501


def test_alphabet_generation_value_exception_with_bad_input():
    bad_input = 0
    with pytest.raises(ValueError):
        AG.generate_alphabet_from_base(bad_input)


def test_default_alphabet_generation_with_base_1():
    base, char_set = 1, ['1']
    assert char_set == AG.generate_alphabet_from_base(
        base, char_set)


def test_default_binary_alphabet_generation():
    binary_chars = base_200_chars_with_defaults[:2]
    assert binary_chars == AG.generate_alphabet_from_base(2)


def test_default_octal_alphabet_generation():
    octal_chars = base_200_chars_with_defaults[:8]
    assert octal_chars == AG.generate_alphabet_from_base(8)


def test_default_hex_alphabet_generation():
    hex_chars = base_200_chars_with_defaults[:16]
    assert hex_chars == AG.generate_alphabet_from_base(16)


def test_default_alphabet_generation_with_base_32():
    base_32_chars = base_200_chars_with_defaults[:32]
    assert base_32_chars == AG.generate_alphabet_from_base(32)


def test_default_alphabet_generation_with_base_64():
    base_64_chars = base_200_chars_with_defaults[:64]
    assert base_64_chars == AG.generate_alphabet_from_base(64)


def test_default_alphabet_generation_with_base_128():
    base_128_chars = base_200_chars_with_defaults[:128]
    assert base_128_chars == AG.generate_alphabet_from_base(128)


def test_default_alphabet_generation_with_base_200():
    assert base_200_chars_with_defaults == AG.generate_alphabet_from_base(200)
