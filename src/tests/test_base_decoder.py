from src.algorithms.base_conversion.BaseDecoder import BaseDecoder as BD  # noqa: E501
from random import randint


def generate_random_int():
    return randint(0, 1_000_000_000_000)


def test_binary_to_base_10_for_36():
    expected_num = int("100100", base=2)
    assert expected_num == BD.decode("100100", 2)


def test_octal_to_base_10_for_36():
    expected_num = int("44", base=8)
    assert expected_num == BD.decode("44", 8)


def test_hex_to_base_10_for_36():
    expected_num = int("24", base=16)
    assert expected_num == BD.decode("24", 16)


def test_binary_to_base_10_for_a_random_number():
    random_num = generate_random_int()
    random_num_encoding = bin(random_num)[2:]
    assert random_num == BD.decode(
        random_num_encoding, 2), f"Faield for: {random_num}"


def test_octal_to_base_10_for_a_random_number():
    random_num = generate_random_int()
    random_num_encoding = oct(random_num)[2:]
    assert random_num == BD.decode(
        random_num_encoding, 8), f"Faield for: {random_num}"


def test_hex_to_base_10_for_a_random_number():
    random_num = generate_random_int()
    random_num_encoding = hex(random_num)[2:]
    assert random_num == BD.decode(
        random_num_encoding, 16), f"Faield for: {random_num}"


def test_base_128_to_base_10_for_a_random_number_with_extended_alphabet():
    expected_num = 2_097_151
    expected_num_encoding = "~~3~~3~~3"
    assert expected_num == BD.decode(expected_num_encoding, 128)
