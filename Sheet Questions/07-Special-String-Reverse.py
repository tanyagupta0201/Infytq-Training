# Problem Link: https://practice.geeksforgeeks.org/problems/special-array-reversal2328/1#

class Solution:
    def reverse(self, s):

        l = 0
        r = len(s) - 1

        # convert string into list
        myList = list(s)

        while l < r:
            if not myList[l].isalpha():
                l += 1
            elif not myList[r].isalpha():
                r -= 1
            else:
                myList[l], myList[r] = myList[r], myList[l]
                l += 1
                r -= 1

        return ''.join(myList)
