from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        i, n = 0, len(ratings)

        # assigning candies from left to right
        left_ro_right = [1] * n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                left_ro_right[i] = left_ro_right[i - 1] + 1

        # assigning candies from right to left
        right_to_left = [1] * n
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_to_left[i] = right_to_left[i + 1] + 1

        res = 0
        # getting max at each children either from left-to-right or right-to-left
        for i in range(n):
            res += max(right_to_left[i], left_ro_right[i])

        return res
