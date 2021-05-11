from src.algorithms.image_manipulation.RandomImageFactory import RandomImageFactory
from src.algorithms.image_manipulation.Resolution import Resolution


def test_image_generation():
    res = Resolution.resolution_factory("4k")
    RandomImageFactory.generate_random_image(res)