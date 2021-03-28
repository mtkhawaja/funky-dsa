# Reference: https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan

class BKBitCounting:

    @classmethod
    def count_bits(cls, number: int) -> int:
        bit_count = 0
        while number:
            number = cls.clear_last_set_bit(number)
            bit_count += 1
        return bit_count

    @classmethod
    def clear_last_set_bit(cls, number: int) -> int:
        return number & (number - 1)
