# Problem: Minimum Distances
# Link: https://www.hackerrank.com/challenges/minimum-distances/problem
# Description:
# Given an array of integers, find the minimum distance between any pair of equal elements.
# The distance between two elements is the absolute difference between their indices.
# If no such pair exists, return -1.
#
# Input:
# a - list of integers
#
# Output:
# Integer representing the minimum distance between any pair of equal elements, or -1 if none exist

def minimumDistances(a):
    b = []
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                t = abs(j - i)
                b.append(t)
    if len(b) >= 1:
        return min(b)
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')
    fptr.close()
