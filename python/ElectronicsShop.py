# Problem: Electronics Shop
# Link: https://www.hackerrank.com/challenges/electronics-shop/problem
# Description:
# A person wants to buy the most expensive combination of one keyboard and one USB drive
# without exceeding their budget. If no combination is possible, return -1.

# Input:
# - First line: three integers b (budget), n (number of keyboards), m (number of drives)
# - Second line: n space-separated integers (keyboard prices)
# - Third line: m space-separated integers (drive prices)

# Output:
# - Single integer: maximum spendable amount or -1 if no valid combination exists

def getMoneySpent(keyboards, drives, b):
    max_spent = -1
    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b:
                max_spent = max(max_spent, total)
    return max_spent

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()
