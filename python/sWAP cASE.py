# Problem: sWAP cASE
# Link: https://www.hackerrank.com/challenges/swap-case/problem
# Description:
# Given a string, swap the case of each character.
# Input:
# s - a string containing alphanumeric characters
# Output:
# A new string with each character's case swapped

def swap_case(s):
    p = ""
    for i in s:
        if i.isupper():
            p += i.lower()
        else:
            p += i.upper()
    return p
