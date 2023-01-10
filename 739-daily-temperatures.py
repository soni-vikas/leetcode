class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # similar to next greater element. 
        next_greator_distance = [0] * len(temperatures)

        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                next_greator_distance[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        for i in stack:
            next_greator_distance[i] = 0

        return next_greator_distance
