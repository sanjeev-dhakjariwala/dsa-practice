import heapq
from typing import *


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        max_heap = [-int(num) for num in nums]
        print(max_heap)
        heapq.heapify(max_heap)
        print(max_heap)
        return str(-max_heap[k - 1])


sol = Solution()
print(sol.kthLargestNumber(["2", "21", "12", "1"], 4))
