def check_palindrome(user_input):
    cleaned_input = _clean_input(user_input)
    cleaned_input.reverse()
    return list(user_input) == cleaned_input and len(cleaned_input) >= 3


def _clean_input(user_input):
    return list(user_input)
