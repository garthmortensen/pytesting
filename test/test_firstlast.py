import pytest
from firstlast import firstlast


# fixtures enable reusing variables across tests
#@pytest.fixture(scope="module")  # if your fixture isnt just a string but perhaps a db connection,
# scope lets you run fixture only once, and prevent reruns
# fixtures work just like global variables, BUT if youre dealing with objects or scopes, then this helps
@pytest.fixture()
def simple_string():
    return "abcd"  # you could use an object template (Person) or a dict, or whatever


def test_simple(simple_string):
    assert firstlast(simple_string) == "ad"


def test_complex(simple_string):
    assert firstlast(simple_string)[0] == "a"

