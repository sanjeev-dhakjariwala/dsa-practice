from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        temp_sum = 0

        for num in nums:
            temp_sum += num
            if temp_sum < 0:
                temp_sum = 0
            max_sum = max(max_sum, temp_sum)

        # return max_sum if max_sum != float('-inf') else -1
        return max_sum


sol = Solution()
print(sol.maxSubArray([-1]))
