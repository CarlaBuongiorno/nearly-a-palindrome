from nearly_a_palindrome import check_palindrome


def test_check_palindrome_exists():
    assert check_palindrome


def test_one_letter_palindrome_is_false():
    assert check_palindrome('a') == False


def test_three_letter_palindrome_is_true():
    assert check_palindrome('aba') == True