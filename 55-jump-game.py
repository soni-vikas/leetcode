from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last = n - 1
        for i in range(n - 1):
            j = n - 2 - i
            if j + nums[j] >= last: last = j

        return last == 0
