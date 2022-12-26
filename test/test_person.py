import pytest
from person import Person


@pytest.mark.parametrize("first_name, last_name, age",
                         [("first", "last", 50),
                          ("pony", "cat", 5),
                          ("goat", "cat", 4)])
def test_create_person(first_name, last_name, age):
    p = Person(first_name, last_name, age)
    assert p.first_name == first_name
    assert p.last_name == last_name
    assert p.age == age


@pytest.mark.parametrize("first_name, last_name, age",
                         [("first", "last", 50),
                          ("pony", "cat", 5),
                          ("goat", "cat", 4)])
def test_greet(first_name, last_name, age):
    p = Person(first_name, last_name, age)
    assert p.greet() == f"Hello {first_name} {last_name}"


def test_invalid_empty_person():
    with pytest.raises(TypeError):
        Person()

