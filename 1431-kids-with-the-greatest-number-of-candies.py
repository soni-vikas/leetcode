class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_from_left = []
        for i in candies:    
            max_from_left.append(i if not max_from_left else max(max_from_left[-1], i))
    
        max_from_right = []
        for i in candies[::-1]: #range(len(candies)-1, -1, -1):    
            max_from_right.insert(0, i if not max_from_right else max(max_from_right[0], i))

        n = len(candies)
        ans = []
        for i in range(n):
            left = True if i == 0 else (candies[i] + extraCandies) >= max_from_left[i-1]
            right = True if i == n-1 else (candies[i] + extraCandies) >= max_from_right[i+1]
            ans.append(left and right)

        return ans
