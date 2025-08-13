# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low <= high:
            mid = (low + high) / 2
            checker = isBadVersion(mid)

            if checker == False:
                low = mid + 1

            elif checker == True:
                firstBadVersion = mid
                high = mid - 1

        return firstBadVersion
