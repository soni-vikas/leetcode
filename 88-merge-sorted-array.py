class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # shift elements to the right
        i = 0
        n1 = len(nums1)
        n2 = len(nums2)
        while i < m:
            nums1[n1 - 1 - i], nums1[m - 1 - i] = nums1[m - 1 - i], nums1[n1 - 1 - i]
            i += 1

        i = n1 - m
        j = 0
        k = 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            k += 1

        while i < n1:
            nums1[k] = nums1[i]
            i += 1
            k += 1

        while j < n2:
            nums1[k] = nums2[j]
            j += 1
            k += 1
