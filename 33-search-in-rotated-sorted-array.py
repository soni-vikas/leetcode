class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        hint: if we divide the array from mid, one of the array would always be sorted. 
        """
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int(high - (high - low) / 2)
            if nums[mid] == target:
                return mid

            # right subarray is sorted
            if nums[mid] < nums[high]:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

            # left subarray is sorted
            else:
                if nums[mid] > target and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1
