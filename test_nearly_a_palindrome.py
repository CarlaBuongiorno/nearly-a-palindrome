from nearly_a_palindrome import check_palindrome


def test_check_palindrome_exists():
    assert check_palindrome


def test_one_letter_palindrome_is_false():
    assert check_palindrome('a') == False


def test_three_letter_palindrome_is_true():
    assert check_palindrome('aba') == True


def test_five_letter_palindrome_is_true():
    assert check_palindrome('tenet') == True


def test_nearly_a_palindrome():
    assert check_palindrome('tenets') == True


def test_nearly_a_palindrome_too_small():
    assert check_palindrome('aardvark') == False
