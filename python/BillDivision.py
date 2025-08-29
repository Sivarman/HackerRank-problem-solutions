# Problem: Bill Division
# Link: https://www.hackerrank.com/challenges/bon-appetit/problem
# Description:
# Two friends, Anna and Brian, are deciding how to split the bill at a dinner.
# Anna didn't eat one of the items, located at index k in the bill list.
# Brian calculates Anna's share by dividing the total bill by 2.
# Your task is to determine whether Brian charged Anna correctly.
# If he did, print "Bon Appetit". Otherwise, print the amount he overcharged.
#
# Input:
# bill - list of integers representing the cost of each item
# k - integer, the index of the item Anna didn't eat
# b - integer, the amount Brian charged Anna
#
# Output:
# Print "Bon Appetit" if the bill was fairly split.
# Otherwise, print the integer amount Brian must refund to Anna.

def bonAppetit(bill, k, b):
    sum1 = 0
    t = bill[k]
    bill.remove(t)
    sum1 = sum(bill)
    a = sum1 // 2
    if a == b:
        print("Bon Appetit")
    else:
        d = b - a
        print(d)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())

    bonAppetit(bill, k, b)
