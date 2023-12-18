from typing import *;

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(temp):
            if len(temp) == n:
                res.append(temp[:])
                return
            
            for i in range(0, n):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                helper(temp)
                temp.pop()

        helper([])
        return res
    
sol = Solution()
print(sol.permute([1, 2,3]))