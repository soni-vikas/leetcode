class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for i in nums:
            max_len = max(max_len, self.get_consecutive_element_len(i, nums_set))
        
        return max_len
    
    def get_consecutive_element_len(self, i, nums_set):
        count = 0
        if i in nums_set:
            k = i
            while k in nums_set:
                nums_set.remove(k)
                count += 1
                k -= 1

            k = i + 1
            while k in nums_set:
                nums_set.remove(k)
                count += 1
                k += 1

        return count
        

