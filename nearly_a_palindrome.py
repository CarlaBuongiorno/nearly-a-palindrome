def check_palindrome(user_input):
    i = list(user_input)
    if len(i) < 3:
        return False
    i.reverse()
    if list(user_input) == i:
        return True
    return False