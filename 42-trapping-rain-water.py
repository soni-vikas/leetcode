from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        # calculate prefix sum from left
        left_max = [0] * n
        for i in range(n):
            if i == 0:
                left_max[i] = height[i]
            else:
                left_max[i] = max(left_max[i - 1], height[i])

        # calculate prefix sum from right
        right_max = [0] * n
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                right_max[i] = height[i]
            else:
                right_max[i] = max(right_max[i + 1], height[i])

        # collect trap water at ith building
        res = 0
        for i in range(1, n - 1):
            trap_water = min(left_max[i - 1], right_max[i + 1]) - height[i]
            if trap_water > 0:
                res += trap_water

        return res
