class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        ************My Code**********
        #midIndex = len(nums) - 1
        midIndex = 0
        leftSum = 0
        rightSum = 0

        def LeftSideSum(start, end):
            ls = 0
            for i in range(start, end):
                ls += nums[i]
            print("LeftSum:", ls)
            return ls

        def RightSideSum(start, end):
            rs = 0
            for i in range(start, end):
                rs += nums[i]
            print("RightSum:", rs)
            return rs

        #while midIndex >= 0:
        while midIndex < len(nums):
            print("midindex:",  midIndex)
            if midIndex == 0:
                rightSum = RightSideSum(midIndex+1, len(nums))
                leftSum = 0
                print("while loop rightsum:", rightSum)
                print("while loop leftsum:", leftSum)

            elif midIndex == len(nums) - 1:
                rightSum = 0
                leftSum = LeftSideSum(0, (midIndex-1)+1)
                print("while loop rightsum:", rightSum)
                print("while loop leftsum:", leftSum)

            else:
                rightSum = RightSideSum(midIndex+1, len(nums))
                leftSum = LeftSideSum(0, (midIndex-1)+1)
                print("while loop rightsum:", rightSum)
                print("while loop leftsum:", leftSum)

            if rightSum == leftSum:
                return midIndex
                break
            elif rightSum != leftSum:
                midIndex = midIndex + 1
                leftSum = 0
                rightSum = 0
        return -1
        '''

        totalSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1
