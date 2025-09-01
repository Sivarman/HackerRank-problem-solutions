# Problem: Divisible Sum Pairs
# Link: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# Description:
# Given an array of integers and a positive integer k, determine the number of (i, j) pairs
# where i < j and ar[i] + ar[j] is divisible by k.

# Input:
# - First line: two space-separated integers n (array size) and k (divisor)
# - Second line: n space-separated integers ar[i] (array elements)

# Output:
# - Single integer: number of valid (i, j) pairs

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')
    fptr.close()
