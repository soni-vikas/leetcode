class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        act_sum = sum(nums)
        exp_sum = int(len(nums) * (len(nums) + 1) / 2)
        return exp_sum - act_sum
