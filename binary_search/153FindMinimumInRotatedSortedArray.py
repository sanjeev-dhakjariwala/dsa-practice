from typing import *


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        res = -1
        while low < high:
            mid = low + (high - low) // 2
            res = mid
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[res]


sol = Solution()
print(sol.findMin([3,1,2]))
