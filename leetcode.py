def removeElement(self, nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
        elif nums[i] != val:
            i += 1

    k = len(nums)
    return k
