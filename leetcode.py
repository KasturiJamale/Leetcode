# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low <= high:
            mid = (low + high) / 2
            guessCheck = guess(mid)

            if guessCheck == 0:
                return mid
            elif guessCheck == 1:
                low = mid + 1
            elif guessCheck == -1:
                high = mid - 1

