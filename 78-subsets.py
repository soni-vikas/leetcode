from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            temp = []
            for s in res:
                temp.append(s + [num])

            res += temp

        return res
