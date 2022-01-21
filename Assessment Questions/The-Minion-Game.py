# Problem Link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    n = len(string)
    vowel = 0
    consonent = 0

    # (n - i) is done to find number of words
    for i in range(n):
        if string[i] in "AEIUO":
            vowel += (n - i)
        else:
            consonent += (n - i)

    if vowel > consonent:
        print("Kevin " + str(vowel))
    elif vowel == consonent:
        print("Draw")
    else:
        print("Stuart " + str(consonent))
