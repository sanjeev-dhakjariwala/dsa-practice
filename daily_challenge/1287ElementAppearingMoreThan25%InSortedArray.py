from typing import *


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hash_set = Counter(arr)
        f = (25 / 100) * len(arr)
        for key, value in hash_set.items():
            if value >= f:
                return key
        return -1


sol = Solution()
print(sol.findSpecialInteger([1, 2, 3, 3]))
