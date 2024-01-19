from typing import *


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        miss = 0
        while True:
            if i not in arr:
                if miss == k:
                    return i
                miss += 1
            i += 1
        return -1

sol = Solution()
print(sol.findKthPositive([2, 3,4,7,11], 5))