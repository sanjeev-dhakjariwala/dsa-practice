from typing import *
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for num in nums:
            if num in nums:
                return True
            else:
                hashSet.append(num)
        return False
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 4]))