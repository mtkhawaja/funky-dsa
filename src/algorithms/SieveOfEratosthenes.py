from __future__ import annotations
from typing import List
from math import sqrt, ceil

# Adapted from:
# https://www.algolist.net/Algorithms/Number_theoretic/Sieve_of_Eratosthenes


class SieveOfEratosthenes:
    @staticmethod
    def generate_primes(end: int) -> List[int]:
        if not _is_valid_input(end):
            return []
        sqrt_of_end = ceil(sqrt(end))
        sequence = [False for _ in range(0, end)]
        for seq_index in range(2, sqrt_of_end):
            if _is_prime(seq_index, sequence):
                _classify_prime_multiples_as_composite(
                    seq_index, end, sequence)
        return _collect_primes(sequence)


def _is_valid_input(end: int) -> bool:
    return end and end > 1


def _is_prime(index: int, sequence: List[int]):
    return not sequence[index]


def _classify_prime_multiples_as_composite(
        prime: int,
        end: int,
        sequence: List[int]):
    for i in range(prime**2, end, prime):
        sequence[i] = True


def _collect_primes(sequence: List[int]):
    return [p for p in range(2, len(sequence)) if not sequence[p]]
