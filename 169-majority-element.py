class Solution:

    def majorityElement(self, nums: List[int]) -> int: 
        res = None
        count = 0

        for i in nums:
            if count == 0:
                res = i
                count += 1

            elif res == i:
                count += 1
            
            else:
                count -= 1
        
        return res
