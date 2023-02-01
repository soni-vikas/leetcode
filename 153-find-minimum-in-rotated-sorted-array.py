from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while abs(r - l) > 1:
            m = int((r + l) / 2)

            if nums[m - 1] > nums[m]:
                return nums[m]

            if nums[m] <= nums[r]:
                r = m

            else:
                l = m

        return min(nums[r], nums[l])
