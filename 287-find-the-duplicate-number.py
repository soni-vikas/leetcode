class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num] < 0:
                return num
            
            nums[num] = -nums[num]

