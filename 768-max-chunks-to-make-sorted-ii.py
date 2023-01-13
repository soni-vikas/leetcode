class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        """
        split after ith position if max_left[i] <= min_right[i+1]
        i.e. if all the elements from left is smaller than or equal to element at ith position & 
        all the elements from right is greator than or equal to element at ith position - split the array from b/w ith & ith+1 position. 
        """

        max_left = []
        for i in arr:
            max_left.append(i if not max_left else max(max_left[-1], i))
        
        min_right = []
        for i in arr[::-1]:
            min_right.insert(0, i if not min_right else min(min_right[0], i))
    
        count = 1
        for i in range(0, len(arr) - 1):
            if max_left[i] <= min_right[i+1]:
                count += 1

        return count


