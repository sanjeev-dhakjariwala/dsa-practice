from typing import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
            return res


sol = Solution()
print(sol.missingNumber([3, 0, 1]))
