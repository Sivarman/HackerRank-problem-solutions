# Problem: Loops
# Link: https://www.hackerrank.com/challenges/python-loops/problem
# Description:
# Given an integer n, print the square of all non-negative integers less than n.
# Input:
# n - an integer (1 ≤ n ≤ 20)
# Output:
# n lines, each containing the square of an integer from 0 to n-1

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)
