from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                s = nums[j] + nums[k] + nums[i]
                if s == 0:
                    ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1

        return list(ans)
