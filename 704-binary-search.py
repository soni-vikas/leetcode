class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchUtil(nums, target, 0, len(nums)-1)

    def searchUtil(self, nums: List[int], target: int, low: int, high: int) -> int:
        if low > high:
            return -1
        
        mid = int(high - (high - low) / 2)
        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            return self.searchUtil(nums, target, low, mid-1)
        
        else:
            return self.searchUtil(nums, target, mid+1, high)
