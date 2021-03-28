from src.algorithms.BKBitCounting import BKBitCounting


def count_bits(num: int) -> int:
    return bin(num).count("1")


def test_when_there_is_one_set_bit():
    num = 8
    expected_bit_count = count_bits(num)
    assert expected_bit_count == BKBitCounting.count_bits(num)


def test_when_there_are_no_set_bits():
    num = 0
    expected_bit_count = count_bits(num)
    assert expected_bit_count == BKBitCounting.count_bits(num)


def test_when_there_are_7_set_bits():
    num = 127
    expected_bit_count = count_bits(num)
    assert expected_bit_count == BKBitCounting.count_bits(num)
