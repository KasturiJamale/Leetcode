class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        print(len(nums))
        i=0

        while i in range(0, len(nums)):
            if nums[i] == target:
                return i

            elif nums[i] >= target:
                return i
            i+=1
        return len(nums)