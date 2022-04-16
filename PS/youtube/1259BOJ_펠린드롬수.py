from types import prepare_class


def palindrome(s):
    return s == s[::-1]


while True:
    s = input()
    if s == '0':
        break
    print('yes' if palindrome(s) else 'no')
