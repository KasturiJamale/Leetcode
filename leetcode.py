class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #print(len(nums))
        elements = len(nums)
        nums = set(nums)
        disappearNums = []

        for i in range(1,elements+1):
            if i not in nums:
                disappearNums.append(i)
        return disappearNums

