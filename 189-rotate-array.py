class Solution:
    def rotate_slice(self, nums: List[int], start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
        return 
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        
        n = len(nums)
        k = k % n
        
        self.rotate_slice(nums, 0, n-k-1)
        self.rotate_slice(nums, n-k, n-1)
        self.rotate_slice(nums, 0, n-1)
        return
