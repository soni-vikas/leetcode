from typing import List


class ListItem:
    def __init__(self, i):
        self.i = i

    def __lt__(self, a):
        return str(self.i) + str(a.i) > str(a.i) + str(self.i)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [ListItem(i) for i in nums]
        print([i.i for i in sorted(nums)])
        return "".join([str(i.i) for i in sorted(nums)]).lstrip("0") or "0"
