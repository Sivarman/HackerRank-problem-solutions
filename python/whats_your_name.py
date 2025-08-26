# Problem: What's Your Name?
# Link: https://www.hackerrank.com/challenges/whats-your-name/problem
# Description:
# Given the first and last name of a person, print a greeting using the full name.
# Input:
# first - first name (string)
# last - last name (string)
# Output:
# Greeting message: "Hello <first> <last>! You just delved into python."

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
