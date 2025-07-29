class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        '''
        count = 0

        for i in range(len(arr1)):
            flag = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    flag = False
                    break

            if flag == True:
                count += 1
        return count
        '''

        arr2.sort()  # Required for binary search
        count = 0

        def isValid(x, arr2, d):
            start = 0
            end = len(arr2) - 1

            while start <= end:
                mid = start + (end - start) // 2
                if abs(arr2[mid] - x) <= d:
                    # Found a value too close to x
                    return False
                elif arr2[mid] < x:
                    start = mid + 1
                else:
                    end = mid - 1

            # No element within distance d
            return True

        for x in arr1:
            if isValid(x, arr2, d):
                count += 1
        return count