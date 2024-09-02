class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        temp_ele = nums[0]
        length = len(nums)

        if len(nums) == 1 and nums[0] == 0:
            return True
        elif len(nums) == 1 and nums[0] == 1:
            return True

        while temp_ele > 0:
            if nums[temp_ele] < length:
                if temp_ele + nums[temp_ele] != length - 1 :
                    temp_ele -= 1
                elif temp_ele + nums[temp_ele] == length - 1:
                    return True
        return False
        '''

        length = len(nums)
        temp_ele = 0
        farthest = 0

        if length == 1:
            return True

        while temp_ele <= farthest:
            farthest = max(farthest, temp_ele + nums[temp_ele])
            if farthest >= length - 1:
                return True
            temp_ele += 1

        return False