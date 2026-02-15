 # Problem: Apple and Orange
# Link: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Description:
# Sam's house is located between points s and t on the x-axis.
# There is an apple tree at point a and an orange tree at point b.
# Apples and oranges fall from their trees at various distances.
# Your task is to determine how many apples and oranges fall on Sam's house.
#
# Input:
# s - integer, start point of Sam's house
# t - integer, end point of Sam's house
# a - integer, location of the apple tree
# b - integer, location of the orange tree
# apples - list of integers, distances each apple falls from tree a
# oranges - list of integers, distances each orange falls from tree b
#
# Output:
# Two integers printed on separate lines:
# - Number of apples that fall on Sam's house
# - Number of oranges that fall on Sam's house

def countApplesAndOranges(s, t, a, b, apples, oranges):
    c, d = 0, 0
    for i in range(len(apples)):
        apples[i] += a
    for j in range(len(oranges)):
        oranges[j] += b

    for i in range(len(apples)):
        if s <= apples[i] <= t:
            c += 1
    for j in range(len(oranges)):
        if s <= oranges[j] <= t:
            d += 1
    print(c)
    print(d)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
