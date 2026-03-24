from app.string_utils import (
    capitalize_words,
    count_vowels,
    is_palindrome,
    reverse_string,
)


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python is fun") == "Python Is Fun"


def test_count_vowels():
    assert count_vowels("hello") == 2  # e, o
    assert count_vowels("aeiou") == 5  # all five vowels
    assert count_vowels("rhythm") == 0  # no vowels


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("Race Car") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man, a plan, a canal: Panama") is True
