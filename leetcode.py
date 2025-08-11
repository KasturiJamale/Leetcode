class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        for i in range(0,len(arr)):
            doubleValue = 2 * arr[i]
            for j in range(0, len(arr)):
                if doubleValue == arr[j] and i != j:
                    return True
                    break
        return False