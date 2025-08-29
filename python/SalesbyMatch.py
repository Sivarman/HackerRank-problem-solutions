# Problem: Sales by Match
# Link: https://www.hackerrank.com/challenges/sock-merchant/problem
# Description:
# Given an array of integers representing the color of each sock in a pile,
# determine how many pairs of socks with matching colors there are.
# A pair is two socks of the same color.
#
# Input:
# n - integer, the number of socks
# ar - list of integers representing sock colors
#
# Output:
# Integer representing the total number of matching pairs

def sockMerchant(n, ar):
    counts = []
    nwcnts = []
    
    for i in set(ar):
        a = ar.count(i)
        counts.append(a)
    for j in counts:
        b = j // 2
        nwcnts.append(b)
    return sum(nwcnts)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()
