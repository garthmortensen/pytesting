# Pytest

![latest_test](https://github.com/garthmortensen/pytesting/actions/workflows/execute_pytest.yaml/badge.svg)

![latest_lint](https://github.com/garthmortensen/pytesting/actions/workflows/execute_linter.yaml/badge.svg)

Explore TDD with pytest and an automated build tool.

## User story

1. As a user, I want to do something.
2. As a user, I want to do something.

## Acceptance criteria

1. It's done when the function returns something.
2. It's done when the function returns something.
3. It's done when the function returns something.

## Background

PyTest is growing in popularity, removes much of the tedious annoying work found with `unittest`, which is modeled after SUnit, JUnit and other testing frameworks backed by TDD creator Kent Beck. 

You can test web apps with it via Selenium. You can also do "monkey patching", which when working with an API means providing synthetic data responses in place of actual call returns. 

## Setup

In order to create a vanilla pytest environment, I'll create `venv/`.

```bash
python -m venv venv
source venv/Scripts/activate  # windows OS
source venv/bin/activate  # linux/mac OS
```

Then check.

```bash
type python
type pip
pip freeze  # display install packages
```

Install pytest.

```bash
pip install pytest
type pytest
```

A popular pytest plugin to improve the terminal output readability is `sugar`. It's not super important, but nice. To install:

```bash
pip install pytest-sugar
```

Tests should have filenames named after function name, e.g.: `test_myfunction.py`

Kick off your tests?

```bash
# test all tests in current and subdirectories:
pytest 
# run 1 test file
pytest test_hello.py
# run 1 test in 1 test file
pytest test_hello.py::test_hello2
```

On linux? Might need to `hash -r` in the local dir.

Other options.

```bash
-v # verbose
-vv # very verbose
```

What about coverage?

```bash
pip install pytest-coverage
```

Then run it with:
```bash
pytest --cov --vv .  # first do this
coverage html  # then convert output to html, i think!
```

Then navigate to the test folder that's created and examine the html file, which you can click into different files in to examine coverage.

## Testing

Big picture, when I call a function with certain inputs, I''ll get certain outputs. If I call a function expecting it to fail, I expect it to fail in a certain way.

Testing doesn't ensure there'll be 0 bugs, but it does ensure that if you fix a bug, it won't recur. If you find a problem, you can write a test to replicate it, then you fix it. 

START TESTING WHEN YOUR CODE IS STILL SIMPLE. You have a tendency not to test simple code. Write for a week, then start writing tests. This makes it very difficult to catchup. 

Test goes in a separate file.

`assert output == "expected output"`

assert just looks to see if what's on the right is True or False, and does something if False.

So, write your code:

```python
# hello.py
def hello(name):
    """returns a greeting"""
    return f"hello {name}!"
```

Write your test:

```python
# test_hello.py
from hello import hello  # treat function as a module


def test_hello():
    output = hello("world")
    assert output == "hello world!"


def test_hello2():
    output = hello("goat")
    assert output == "hello goat!"
```

Run pytest:

```bash
$ pytest
============================================================================================ test session starts =============================================================================================
platform win32 -- Python 3.9.7, pytest-7.1.2, pluggy-1.0.0
rootdir: G:\My Drive\github\pytesting
plugins: anyio-3.5.0
collected 2 items                                                                                                                                                                                             
code\test_hello.py ..                                                                                                                                                                                   [100%] 
============================================================================================= 2 passed in 0.19s ============================================================================================== 
```

You should write passing tests and failing tests. Tests are written to pass. Assert always assumes True on right, so you write to test if None returns. Look for the positive side of things.

Mutation testing = let software change your code and make sure you've covered all positive and negative cases correctly.

/test/ directory. Move tests into here. Now place a 100% empty file in /test/ named `__init__.py` and python will search and find all tests.

`sys.path` shows you where python will look for modules.

Trying to fix a failed test case? Tweak then run the previously failed test:

```bash
pytest --last-failed
```

## Improving tests

This is a starting point.

```python
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
```

Criticism is that this is highly repetitive. You want to DRY up this code.

```python
@pytest.mark.parametrize("word, count",
                            [("hello", 2),
                             ("d3oody", 3),
                             ("HELLO", 2),
                             ("D3OODY", 3),
                             ("123", 0),
                             ("", 0),
                             ("zzz xxc", 0),
                             ])


def test_count_vowels_parametrizzz(word, count):
    assert count_vowels(word) == count
```

Output:

```bash
test/test_counting.py::test_count_vowels_parametrizzz[hello-2] PASSED         [  5%] 
test/test_counting.py::test_count_vowels_parametrizzz[d3oody-3] PASSED        [ 11%]
test/test_counting.py::test_count_vowels_parametrizzz[HELLO-2] PASSED         [ 16%] 
test/test_counting.py::test_count_vowels_parametrizzz[D3OODY-3] PASSED        [ 22%] 
test/test_counting.py::test_count_vowels_parametrizzz[123-0] PASSED           [ 27%] 
test/test_counting.py::test_count_vowels_parametrizzz[-0] PASSED              [ 33%] 
test/test_counting.py::test_count_vowels_parametrizzz[zzz xxc-0] PASSED       [ 38%]
test/test_counting.py::test_count_vowels_simple PASSED                        [ 44%] 
test/test_counting.py::test_count_vowels_ucase PASSED                         [ 50%] 
test/test_counting.py::test_count_vowels_int PASSED                           [ 55%] 
test/test_counting.py::test_count_vowels_empty PASSED                         [ 61%] 
test/test_counting.py::test_count_vowels_no_vowels PASSED                     [ 66%] 
test/test_counting.py::test_count_vowels_list PASSED                          [ 72%] 
# ...other tests as well
```

So, using the parameterized approach, you can add many new tests without adding new functions. You could even programmatically create the test tuples. This isn't good for catching exceptions, but good at testing strange or edge cases.

## Black linter

Format code with Black linter before push using

```bash
black filename.py
```

This tool was mentioned in Beyond the Basics python book, around page 55.
