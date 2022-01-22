# Problem Link: https://practice.geeksforgeeks.org/problems/factors-sum2016/1/#

import math


class Solution:
    def factorSum(self, N):
        if(N == 1):
            return 1

        s = 0
        for i in range(2, (int)(math.sqrt(N)) + 1):
            if N % i == 0:
                if i == (N / i):
                    s += i
                else:
                    s += i + (N // i)

        return s + 1 + N
