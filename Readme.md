# Pytest

Explore TDD with pytest.

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

1h









