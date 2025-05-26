class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

        outputArr = []
        for i in range(len(arr)):
            if arr[i] == 0:
                outputArr.append(arr[i])
                outputArr.append(arr[i])
            else:
                outputArr.append(arr[i])

        for i in range(len(arr)):
            arr[i] = outputArr[i]
