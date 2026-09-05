class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first < second:
                new = first - second
                heapq.heappush(heap, new)
            elif first > second:
                new = second - first
                heapq.heappush(heap, new)
            
        return abs(heap[0]) if heap else 0