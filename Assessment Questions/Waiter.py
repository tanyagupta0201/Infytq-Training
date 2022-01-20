# Problem Link: https://www.hackerrank.com/challenges/waiter/problem

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#


def waiter(number, q):

    # find all prime numbers and store it in a list p
    p = []

    def isPrime(n):
        for j in range(2, int(n / 2) + 1):
            if n % j == 0:
                return False
            return True

        # According to constraints take value till 10000
    for n in range(2, 10000):
        if(isPrime(n)):
            p.append(n)

    A = []
    B = []
    answer = []

    for i in range(q):
        # pop out all the numbers from stack 'number'
        while(number):
            val = number.pop()
            if val % p[i] == 0:
                B.append(val)
            else:
                A.append(val)

        # Now pop out all elements from B and store it in answer
        while(B):
            answer.append(B.pop())

        number = A
        A = []

    # if any elements left in the number array after the iteration is over
    while(number):
        answer.append(number.pop())
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
