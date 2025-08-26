# Problem: Print Function
# Link: https://www.hackerrank.com/challenges/python-print/problem
# Description:
# Given an integer n, print the numbers from 1 to n without spaces or newlines.
# Input:
# n - an integer (1 ≤ n ≤ 150)
# Output:
# A single line containing the numbers from 1 to n concatenated

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")
