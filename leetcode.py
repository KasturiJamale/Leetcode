class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        temp = [0] * len(nums1)

        i = 0
        j = 0
        k = 0
        print("Index k :", k)

        while i < m and j < n and k < len(temp):
            if nums1[i] <= nums2[j]:
                temp[k] = nums1[i]
                i += 1
            else:
                temp[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            temp[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            temp[k] = nums2[j]
            j += 1
            k += 1

        print(temp)
        nums1[:] = temp



