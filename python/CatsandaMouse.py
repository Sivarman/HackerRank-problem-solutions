# Problem: Cats and a Mouse
# Link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# Description:
# Two cats (Cat A and Cat B) and a mouse (Mouse C) are positioned on a line.
# Each cat moves at the same speed toward the mouse.
# Your task is to determine which cat will catch the mouse first.
# If both cats reach the mouse at the same time, the mouse escapes.
#
# Input:
# x - integer, position of Cat A
# y - integer, position of Cat B
# z - integer, position of Mouse C
#
# Output:
# String: "Cat A", "Cat B", or "Mouse C" depending on which cat reaches the mouse first

def catAndMouse(x, y, z):
    r = abs(x - z)
    t = abs(y - z)
    if r == t:
        return 'Mouse C'
    if r > t:
        return 'Cat B'
    else:
        return 'Cat A'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        fptr.write(result + '\n')

    fptr.close()
