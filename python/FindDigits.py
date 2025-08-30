# Problem: Find Digits
# Link: https://www.hackerrank.com/challenges/find-digits/problem
# Description:
# Given an integer n, count how many of its digits evenly divide n.
# Ignore digits that are zero (as division by zero is undefined).
#
# Input:
# t - number of test cases
# For each test case:
#   n - integer to analyze
#
# Output:
# For each test case, print the count of digits in n that evenly divide n.

def findDigits(n):
    count = 0
    original = n
    while n > 0:
        digit = n % 10
        if digit != 0 and original % digit == 0:
            count += 1
        n //= 10
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        result = findDigits(n)
        fptr.write(str(result) + '\n')

    fptr.close()
