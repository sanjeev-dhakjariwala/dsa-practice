class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j, m, n):
            if i > m or j > n:
                return 0
            if i == m and j == n:
                return 1
            down = helper(i + 1, j, m, n)
            right = helper(i, j + 1, m, n)
            return down + right
        return helper(0, 0, m, n)

sol = Solution()
print(sol.uniquePaths(0, 0, 3, 2))