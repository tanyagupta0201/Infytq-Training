# Problem Link: https://meganaukri.com/infytq-exam-questions/

import math


def pronic(n):
    i = 0
    while i <= (int)(math.sqrt(n)):
        if i * (i + 1) == n:
            return True
        i += 1

    return False


s = input()
list = [s[i: j + 1] for i in range(len(s)) for j in range(i, len(s))]

out = set()  # to remove duplicates in the output
for i in list:
    if pronic(int(i)):
        out.add(int(i))

print(out)
