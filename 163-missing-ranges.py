from typing import List

update_range = lambda l, u: str(l) if l == u else "%d->%d" % (l, u)


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ranges = []

        i, n = 0, len(nums)
        while i < n:
            # update range
            if nums[i] > lower:
                ranges.append(update_range(lower, nums[i] - 1))

            # skip all continues nums
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1

            lower = nums[i] + 1
            i += 1

        if lower <= upper:
            ranges.append(update_range(lower, upper))

        return ranges
