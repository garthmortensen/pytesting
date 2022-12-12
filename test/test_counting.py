from counting import count_vowels
import pytest  # only have to do this if we want to import extended functionality


def test_count_vowels_simple():
    assert count_vowels("hello") == 2
    assert count_vowels("d3oody") == 3


def test_count_vowels_ucase() -> None:  # FYI, tests return nothing
    assert count_vowels("HELLO") == 2
    assert count_vowels("D3OODY") == 3


def test_count_vowels_int():
    assert count_vowels("123") == 0


def test_count_vowels_empty():
    assert count_vowels("") == 0


def test_count_vowels_no_vowels():
    assert count_vowels("zzz xxc") == 0


def test_count_vowels_list():
    """exceptions are not returned, so you cant use Try: Except:
    To handle this, we have to import pytest
    We know this will fail. We know we won't get a value back.
    We expect it to fail with AttributeError!
    But we stay reasonable and not try handling all errors"""
    with pytest.raises(AttributeError):
        count_vowels(['aaab'])


# we can DRY up the tests above via parameterized tests
@pytest.mark.parametrize("word, count",  # 1. string with comma separated variable names
                            [("hello", 2),  # 2. list of tuples with left vs right
                             ("d3oody", 3),
                             ("HELLO", 2),
                             ("D3OODY", 3),
                             ("123", 0),
                             ("", 0),
                             ("zzz xxc", 0),
                             ])


def test_count_vowels_parametrizzz(word, count):  # 3. variables are params for function
    assert count_vowels(word) == count  # 4. use params in the test
