from typing import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
            while stack and stack[-1][1] < temperatures[i]:
                idx, ele = stack.pop()
                res[idx] = i - idx
            stack.append((i, temperatures[i]))

        return res


sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
