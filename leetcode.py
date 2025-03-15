class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return None
        if len(nums) == 1:
            return nums

        zeros_count = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        # print(nums)
        nums.extend([0] * zeros_count)

