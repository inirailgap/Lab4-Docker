#!/usr/bin/python
# user_input.py

def is_palindrome(text, m_re):
    return text == m_re

my_string = raw_input('Type the String: ')
my_reverse = my_string[::-1]

print my_reverse
print my_string

if (is_palindrome(my_string, my_reverse)):
    print("YES")
else:
    print("NO")
