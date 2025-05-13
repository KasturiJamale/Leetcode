class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        joinDigits = int("".join(map(str, digits)))
        addOne = joinDigits + 1

        digits = list(map(int, str(addOne)))
        return digits