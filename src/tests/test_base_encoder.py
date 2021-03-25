from src.algorithms.base_conversion.BaseEncoder import BaseEncoder as BE  # noqa: E501
from random import randint


def generate_random_int():
    return randint(0, 1_000_000_000_000)


def test_base_10_to_binary_encoding_for_36():
    expected_string = "100100"
    assert expected_string == BE.encode(36, 2)


def test_base_10_to_octal_encoding_for_36():
    expected_string = "44"
    assert expected_string == BE.encode(36, 8)


def test_base_10_to_hex_encoding_for_36():
    expected_string = "24"
    assert expected_string == BE.encode(36, 16)


def test_base_10_to_binary_encoding_for_a_random_num():
    random_num = generate_random_int()
    expected_string = bin(random_num)[2:]
    assert expected_string == BE.encode(
        random_num, 2), f"Faield for: {random_num}"


def test_base_10_to_octal_encoding_for_a_random_num():
    random_num = generate_random_int()
    expected_string = oct(random_num)[2:]
    assert expected_string == BE.encode(
        random_num, 8), f"Faield for: {random_num}"


def test_base_10_to_hex_encoding_for_a_random_num():
    random_num = generate_random_int()
    expected_string = hex(random_num)[2:]
    assert expected_string == BE.encode(
        random_num, 16), f"Faield for: {random_num}"
