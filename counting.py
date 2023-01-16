def count_vowels(
    word: str,
) -> int:  # typehinting has no impact, unless pip install mypy, which checks typing `mypy count_vowels.py`
    """Count the vowels in a string"""
    total = 0
    for letter in word.lower():
        if letter in "aeiouy":
            total += 1

    return total
