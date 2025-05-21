class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictionary = {}
        output = []

        for item in nums:
            dictionary[item] = dictionary.get(item, 0) + 1

        for key, value in dictionary.items():
            if value == 2:
                output.append(key)

        new_array = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in new_array:
                output.append(i)

        return output

