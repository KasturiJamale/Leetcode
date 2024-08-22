def removeDuplicates(nums: list[int]) -> int:
    i = 0

    while i < len(nums):
        j = i + 1
        count = 0
        while j < len(nums) and nums[i] == nums[j]:
            count += 1
            print("j, count", j, count)
            if count > 1:
                del nums[j]
            else:
                j+=1
        i=j
    return len(nums)

nums = [0,0,1,1,1,1,2,3,3]
value = removeDuplicates(nums)
print(value)


