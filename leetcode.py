class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxValue = 0
        maxNum = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                maxValue += 1
            else:
                maxValue = 0
            maxNum = max(maxValue, maxNum)
        return maxNum
