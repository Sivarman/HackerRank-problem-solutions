# Problem: Grading Students
# Source: https://www.hackerrank.com/challenges/grading/problem

# HackerLand University has a grading policy:
# - Any grade less than 40 is a failing grade.
# - If the difference between the grade and the next multiple of 5 is less than 3,
#   round the grade up to the next multiple of 5.
# - If the grade is less than 38, no rounding occurs as it remains a failing grade.

# Input:
# - grades: List of integers representing student grades

# Output:
# - List of integers representing final grades after rounding

def gradingStudents(grades):
    for i in range(0, len(grades)):
        if(grades[i] < 38):
            pass
        else:
            a = 5 - (grades[i] % 5)
            b = a + grades[i]
            c = abs(grades[i] - b)
            if(c < 3):
                grades[i] = b
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
