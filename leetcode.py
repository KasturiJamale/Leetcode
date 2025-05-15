class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        outputarray = []

        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    for k in range(j+1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            outputarray.append(nums2[k])
                            found = True
                        break
                    break  # Exit loop after finding the element in nums2
            if not found:
                outputarray.append(-1)
        return outputarray
        '''

        outputarray = []

        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    # Start checking from j+1 forward
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            outputarray.append(nums2[k])
                            found = True
                            break
                    if not found:
                        outputarray.append(-1)
                    break  # Break after nums2[j] == nums1[i] is found
        return outputarray