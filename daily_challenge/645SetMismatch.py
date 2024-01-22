from typing import *


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        diff = abs(actual_sum - expected_sum)
        num_set = set()
        duplicate = None

        for num in nums:
            if num in num_set:
                duplicate = num
            num_set.add(num)

        original = diff - duplicate

        return [duplicate, original]


sol = Solution()
print(sol.findErrorNums([1, 2, 2, 4]))
