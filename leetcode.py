class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        maxSum = 0

        for i in range(0, len(nums), 2):
            maxSum += nums[i]
        return maxSum