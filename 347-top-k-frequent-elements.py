import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0)
            count[i] += 1
        
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val for _, val in heap]
        
