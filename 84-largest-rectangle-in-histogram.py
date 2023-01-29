from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # finding minmum in the left
        stack = []
        minimum_from_left = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            minimum_from_left.append((stack[-1] + 1) if stack else 0)
            stack.append(i)

        # finding minmum in the left
        stack = []
        minimum_from_right = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            minimum_from_right.append((stack[-1] - 1) if stack else len(heights) - 1)
            stack.append(i)

        minimum_from_right = minimum_from_right[::-1]

        # find the maximum rectangle possible including ith bar
        ans = 0
        for i in range(len(heights)):
            ans = max(ans, (minimum_from_right[i] - minimum_from_left[i] + 1) * heights[i])
        return ans
