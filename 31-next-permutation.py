from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n <= 1:
            return

        j = n - 2

        # finding index where nums[j] < nums[j+1]
        while j >= 0 and nums[j] >= nums[j + 1]:
            j -= 1

        if j >= 0:
            # replace jth element with next higher number right in the array.
            k = n - 1
            while nums[k] <= nums[j]:
                k -= 1

            nums[j], nums[k] = nums[k], nums[j]

        j += 1
        while j < n - 1:
            nums[j], nums[n - 1] = nums[n - 1], nums[j]
            n -= 1
            j += 1
