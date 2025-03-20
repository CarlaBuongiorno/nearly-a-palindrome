'''Write a function that takes a string, and returns True if that string is a palindrome,
or if it's nearly a palindrome. "Nearly a palindrome" is defined as "a palindrome with extra letters as the end."
Minimum length of the palindrome part is 3 characters.

Examples:

poop -> True
crap -> False
Madam, I'm Adam -> True
tent -> False
tenet -> True
tenets -> True (extra letters at the end, so it's nearly a palindrome)
babble -> True (extra letters at the end, "bab" is a palindrome)
levelling -> True (extra letters at the end)
lotto -> False ("otto" is palindromic, but the extra letter is at the *start*, so it doesn't count.)
aardvark -> False (i suppose "aa" is a palindrome, but it's too short to count.)'''

from nearly_a_palindrome import check_palindrome


def main():
    user_input = input('Please type your palindrome: ')
    palindrome = check_palindrome(user_input)
    print(palindrome)


if __name__ == '__main__':
    main()
