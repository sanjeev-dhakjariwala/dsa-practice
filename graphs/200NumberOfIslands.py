from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                print(f"Visiting cell ({i}, {j})")
                grid[i][j] = '0'  # Mark the current land as visited
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
            else:
                print(f"Returning from cell ({i}, {j})")

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    print(f"Starting DFS for island {islands} at cell ({i}, {j})")
                    dfs(i, j)

        return islands


sol = Solution()
print(sol.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
