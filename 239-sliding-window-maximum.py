import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dequeue = []
        ans = []
        for i, v in enumerate(nums):
            while dequeue and dequeue[-1][1] <= v:
                dequeue.pop(-1)

            while dequeue and dequeue[0][0] <= i - k:
                dequeue.pop(0)

            dequeue.append((i, v))
            if i >= k-1:
                ans.append(dequeue[0][1])
        
        return ans
