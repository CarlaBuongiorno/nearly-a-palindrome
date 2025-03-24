def check_palindrome(user_input):
    cleaned_input = _clean_input(user_input)
    reversed_input = cleaned_input[::-1]
    while reversed_input != cleaned_input:
        cleaned_input, reversed_input = _remove_excess_letters(cleaned_input, reversed_input)
    return len(cleaned_input) >= 3


def _clean_input(user_input):
    return [i.lower() for i in user_input if i.isalnum()]


def _remove_excess_letters(cleaned_input, reversed_input):
        cleaned_input.pop()
        reversed_input.pop(0)
        return cleaned_input, reversed_input