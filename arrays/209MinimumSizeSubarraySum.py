from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        min_len = float('inf')
        current_sum = 0

        while right < n:
            current_sum += nums[right]
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
            right += 1

        return min_len if min_len != float('inf') else 0

sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
