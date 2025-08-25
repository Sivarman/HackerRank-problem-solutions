# Problem: Mutations
# Link: https://www.hackerrank.com/challenges/python-mutations/problem
# Description:
# You are given a string, and a position and character. You need to mutate the string by
# replacing the character at the given position with the new character.
#
# Input:
#   string - the original string
#   position - index (0-based) where the character should be replaced
#   character - the new character to insert
#
# Output:
#   mutated string

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    pos, char = input().split()
    result = mutate_string(s, int(pos), char)
    print(result)
