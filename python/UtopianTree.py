# Problem: Utopian Tree
# Link: https://www.hackerrank.com/challenges/utopian-tree/problem
# Description:
# The Utopian Tree grows in two cycles each year:
# - Spring: height doubles
# - Summer: height increases by 1 meter
# A sapling starts at 1 meter tall. Given n growth cycles, determine the final height.
#
# Input:
# t - number of test cases
# For each test case:
#   n - integer, number of growth cycles
#
# Output:
# For each test case, print the final height of the tree after n cycles

def utopianTree(n):
    sum = 1
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum *= 2
        else:
            sum += 1
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        fptr.write(str(result) + '\n')

    fptr.close()

