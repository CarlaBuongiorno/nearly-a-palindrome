import pytest

from nearly_a_palindrome import check_palindrome


def test_check_palindrome_exists():
    assert check_palindrome


@pytest.mark.parametrize('user_input, expected', [
    ('a',               False),
    ('aba',             True),
    ('tenet',           True),
    ('tenets',          True),
    ('aardvark',        False),
    ('levelling',       True),
    ('lotto',           False),
    ('babble',          True),
    ("madam, i'm adam", True),
    ("Madam, I'm Adam", True),
])
def test_nearly_a_palindrome(user_input, expected):
    assert check_palindrome(user_input) == expected