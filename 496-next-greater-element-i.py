class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greator = [0] * len(nums2)
        ans_dict = {k: -1 for k in nums1}
        
        stack = []
        for i in nums2[::-1]:
            while stack and stack[-1] <= i:
                stack.pop()
            
            if i in ans_dict:
                ans_dict[i] = stack[-1] if stack else -1

            stack.append(i)
        
        return [ans_dict[k] for k in nums1]

