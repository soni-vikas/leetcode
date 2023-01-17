class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for i in nums: 
            if i == 0:
                zero_count += 1
                if zero_count == 2:
                    return [0] * len(nums)
            
            else:
                product *= i
            
        ans = []
        for i in nums:
            if zero_count:
                ans.append(product if i == 0 else 0)

            else:
                ans.append(int(product / i))

        return ans
