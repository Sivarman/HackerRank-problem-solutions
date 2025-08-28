# Problem: Python If-Else
# Link: https://www.hackerrank.com/challenges/py-if-else/problem
# Description:
# Given an integer n, determine whether it is "Weird" or "Not Weird" based on the following rules:
# - If n is odd → "Weird"
# - If n is even and in the inclusive range of 2 to 5 → "Not Weird"
# - If n is even and in the inclusive range of 6 to 20 → "Weird"
# - If n is even and greater than 20 → "Not Weird"

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
