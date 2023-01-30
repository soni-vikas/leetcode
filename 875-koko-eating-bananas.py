import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        res = high
        while low <= high:
            mid = int(high - (high - low) / 2)
            _sum = sum([math.ceil(p / mid) for p in piles])
            if _sum <= h:
                res = min(res, mid)
                high = mid - 1

            else:
                low = mid + 1

        return res
