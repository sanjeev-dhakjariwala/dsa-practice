from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, temp, depth):
            if i == n:
                res.append(temp[:])
                return
            res.append(temp[:])
            for j in range(i, n):
                temp.append(nums[j])
                print("  " * depth, f"helper({j + 1}, {temp})")
                helper(j + 1, temp, depth + 1)
                temp.pop()
        helper(0, [], 0)
        return res

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []

    #     def dfs(i, subSet):
    #         if i == len(nums):
    #             res.append(subSet.copy())
    #             return
    #         subSet.append(nums[i])
    #         dfs(i + 1, subSet)
    #         subSet.pop()
    #         dfs(i + 1, subSet)
    #     dfs(0, [])
    #     return res


# Example usage:
solution = Solution()
result = solution.subsets([1, 2, 3])
print("Final result:", result)
