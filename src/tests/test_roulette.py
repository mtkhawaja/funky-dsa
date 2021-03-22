from src.structures.roulette.Roulette import Roulette


def test_object_creation():
    random_obj = Roulette.roll()
    assert random_obj is not None
