from hello import hello  # treat function as a module


def test_hello():
    output = hello("world")
    assert output == "hello world!"


def test_hello2():
    output = hello("goat")
    assert output == "hello goat!"


def test_hello3():
    output = hello("pony")
    assert output == "hello pony!"
