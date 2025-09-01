# Problem: The Hurdle Race
# Link: https://www.hackerrank.com/challenges/the-hurdle-race/problem
# Description:
# A character can jump up to height k naturally. To clear hurdles taller than k,
# they must drink a magic potion that increases their jump height by 1 per dose.
# Given the list of hurdle heights, determine the minimum number of doses required.

# Input:
# - First line: two space-separated integers n (number of hurdles) and k (max jump height)
# - Second line: n space-separated integers height[i] (height of each hurdle)

# Output:
# - Single integer: minimum number of doses required to clear all hurdles

def hurdleRace(k, height):
    max_hurdle = max(height)
    return max(0, max_hurdle - k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))
    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')
    fptr.close()
