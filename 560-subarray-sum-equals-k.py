class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        
        prefix_sum = {0: 1}
        current_prefix_sum = 0
        for i in nums:
            current_prefix_sum += i
            if (current_prefix_sum - k) in prefix_sum:
                count += prefix_sum[current_prefix_sum - k]
            
            prefix_sum[current_prefix_sum] = prefix_sum.get(current_prefix_sum, 0) + 1

        return count
