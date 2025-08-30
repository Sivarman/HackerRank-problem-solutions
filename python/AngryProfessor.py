# Problem: Angry Professor
# Link: https://www.hackerrank.com/challenges/angry-professor/problem
# Description:
# A professor will cancel class if fewer than k students are present on time.
# Arrival times <= 0 mean the student was on time; > 0 means late.
# Determine if the class is cancelled for each test case.
#
# Input:
# t - number of test cases
# For each test case:
#   n - number of students
#   k - cancellation threshold
#   a - list of arrival times
#
# Output:
# For each test case, print "YES" if class is cancelled, otherwise "NO"

def angryProfessor(k, a):
  b=0
    for i in range(0,len(a)):
        if(a[i]<=0):
            b+=1
    if(b>=k):
        return 'NO'
    else:
        return 'YES'    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().rstrip().split())
        a = list(map(int, input().rstrip().split()))
        result = angryProfessor(k, a)
        fptr.write(result + '\n')

    fptr.close()
