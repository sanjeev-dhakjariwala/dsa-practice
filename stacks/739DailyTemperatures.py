from typing import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            c = 0
            for j in range(i + 1, n - 1):
                c += 1
                if temperatures[i] < temperatures[j]:
                    break
            res.append(c)

        res.append(0)
        return res


sol = Solution()
print(sol.dailyTemperatures([30, 40, 50, 60]))
