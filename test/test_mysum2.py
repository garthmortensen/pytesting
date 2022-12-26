import pytest
from mysum2 import mysummation
import random

# $ pytest . -s -vv


def test_mysummation_simple():
    assert mysummation([10, 20, 30]) == 60


def test_mysummation_positives():
    assert mysummation([1, 2, 3]) == 6
    assert mysummation([1, 2, 3, 4, 5]) == 15


# @pytest.mark.negative
def test_mysummation_negatives():
    assert mysummation([1, -10]) == -9


# @pytest.mark.nonint
def test_mysummation_negatives():
    assert mysummation([1, 0.5]) == 1.5


# @pytest.mark.negative
# @pytest.mark.nonint
def test_mysummation_negatives():
    assert mysummation([-1, 0.5]) == -0.5


def test_mysummation_bad_floats():
    assert pytest.approx(mysummation([0.1, 0.2])) == 0.3


# generate random numbers at test runtime, and dont regenerate for each test
@pytest.fixture(scope="module")
def standard_numbers():  # fixture will produce random numbers each execution
    numbers = [random.randint(0, 100) for i in range(5)]
    return numbers, sum(numbers)


def test_standard_numbers(standard_numbers):
    numbers, total = standard_numbers
    print(f"{numbers=}, {total=}")  # py3.8 f-strings with = print values
    assert mysummation(numbers) == total

