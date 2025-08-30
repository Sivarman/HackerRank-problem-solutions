# Problem: Viral Advertising
# Link: https://www.hackerrank.com/challenges/strange-advertising/problem
# Description:
# HackerLand Enterprise launches a viral ad campaign. On day 1, the ad is shared with 5 people.
# Each day, half of the recipients like the ad and each shares it with 3 new people the next day.
# Determine the cumulative number of likes after n days.
#
# Input:
# n - integer, number of days the campaign runs
#
# Output:
# Integer: total number of people who liked the ad over n days

def viralAdvertising(n):
    shared = 5
    total_likes = 0
    for _ in range(n):
        liked = shared // 2
        total_likes += liked
        shared = liked * 3
    return total_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')

    fptr.close()
