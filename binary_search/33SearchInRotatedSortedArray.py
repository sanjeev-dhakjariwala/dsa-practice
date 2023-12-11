from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[low]:
                if nums[mid] < target or nums[low] > target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] < target or nums[low] > target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


sol = Solution()
print(sol.search([5, 1, 3], 5))
