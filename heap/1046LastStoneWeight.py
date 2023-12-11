import heapq
from typing import *


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            a = -heapq.heappop(max_heap)
            b = -heapq.heappop(max_heap)

            if a != b:
                new_stone = a - b
                heapq.heappush(max_heap, -new_stone)

        return abs(max_heap[0]) if max_heap else 0


sol = Solution()
print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))
