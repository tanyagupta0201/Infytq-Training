# Problem Explanation: https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/

class Solution:
    def transform(self, A, B):
        m = len(A)
        n = len(B)

        if m != n:
            return -1

        freq = [0] * 256

        for i in range(m):
            freq[ord(A[i])] += 1

        for i in range(m):
            freq[ord(B[i])] -= 1

        for i in range(256):
            if freq[i]:
                return -1

        i = n - 1
        j = n - 1
        ans = 0

        while i >= 0:

            while i >= 0 and A[i] != B[j]:
                i -= 1
                ans += 1

            if i >= 0:
                i -= 1
                j -= 1

        return ans
