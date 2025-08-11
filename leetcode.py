class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # If negative numbers return false
        if num < 0:
            return False

        # 0 is considered to be perfect square
        if num == 0:
            return True

        low = 1
        high = num

        while low <= high:

            mid = (low + high) / 2
            square = mid * mid

            if square == num:
                return True
            elif square > num:
                high = mid - 1
            elif square < num:
                low = mid + 1

        return False