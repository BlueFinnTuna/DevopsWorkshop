def reverse_string(s):
    return s[::-1]


def capitalize_words(s):
    return s.title()


def count_vowels(s):
    """Count the number of vowels in a string."""
    # BUG: This is missing 'u' from the vowel list!
    return sum(1 for char in s.lower() if char in "aei")


def is_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
