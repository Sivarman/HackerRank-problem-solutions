# Problem: Library Fine
# Link: https://www.hackerrank.com/challenges/library-fine/problem
# Description:
# Given the expected and actual return dates for a library book, calculate the fine.
# Fee structure:
# - If the book is returned on or before the expected return date → fine = 0
# - If returned after the expected day but within the same month and year → fine = 15 × days late
# - If returned after the expected month but within the same year → fine = 500 × months late
# - If returned after the expected year → fixed fine = 10000
#
# Input:
# d1, m1, y1 - actual return date (day, month, year)
# d2, m2, y2 - expected return date (day, month, year)
#
# Output:
# Integer representing the fine

def libraryFine(d1, m1, y1, d2, m2, y2):
    if (y1 == y2) and (m1 == m2):
        if d1 <= d2:
            return 0
        else:
            return 15 * abs(d1 - d2)
    elif (y1 < y2) or (y1 == y2 and m1 < m2):
        return 0
    elif (y1 == y2 and m1 > m2):
        return 500 * abs(m1 - m2)
    else:
        return 10000

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    d1 = int(first_multiple_input[0])
    m1 = int(first_multiple_input[1])
    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()
    d2 = int(second_multiple_input[0])
    m2 = int(second_multiple_input[1])
    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')
    fptr.close()
