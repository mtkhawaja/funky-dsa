from src.algorithms.SieveOfEratosthenes import SieveOfEratosthenes as Sieve
from sympy import primerange, prime
from random import randint


def create_valid_primes_upto(end: int):
    return list(primerange(0, end))


def test_if_zero_returns_empty_list():
    assert [] == Sieve.generate_primes(0)


def test_if_one_returns_empty_list():
    assert [] == Sieve.generate_primes(1)


def test_if_none_returns_empty_list():
    assert [] == Sieve.generate_primes(None)


def test_prime_generation_between_0_to_100():
    known_primes = create_valid_primes_upto(100)
    assert known_primes == Sieve.generate_primes(100)


def test_prime_generation_with_ending_limit_being_composite():
    known_primes = create_valid_primes_upto(10000)
    assert known_primes == Sieve.generate_primes(10000)


def test_prime_generation_with_ending_limit_being_a_prime():
    known_primes = create_valid_primes_upto(18061)
    assert known_primes == Sieve.generate_primes(18061)


def test_prime_generation_between_0_to_Random():
    random_end = randint(2, 20000)
    known_primes = list(primerange(0, random_end))
    assert known_primes == Sieve.generate_primes(
        random_end), f"Test failed with upper limit: {random_end}"


def test_prime_generation_between_0_to_random_prime_ending():
    random_prime_end = prime(randint(2, 20000))
    known_primes = list(primerange(0, random_prime_end))
    known_primes = create_valid_primes_upto(random_prime_end)
    assert known_primes == Sieve.generate_primes(
        random_prime_end), (
        f"Test failed with upper prime limit: {random_prime_end}"
    )
