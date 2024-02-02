from typing import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def helper(curr_index):
            if curr_index == n - 1:
                return True

            max_jump = min(curr_index + nums[curr_index], n - 1)
            for i in range(curr_index + 1, max_jump + 1):
                if helper(i):
                    return True

            return False
        return helper(0)


sol = Solution()
print(sol.canJump([3, 2, 1, 0, 4]))
