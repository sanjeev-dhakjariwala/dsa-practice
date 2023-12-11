from typing import *


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        res = []
        prev_count = 0
        nums = []

        for word in words:
            if word == "prev":
                prev_count += 1
                if prev_count <= len(nums):
                    res.append(nums[-prev_count])
                else:
                    res.append(-1)
            else:
                num = int(word)
                nums.append(num)
                prev_count = 0

        return res


sol = Solution()
print(sol.lastVisitedIntegers(["1", "prev", "2", "prev", "prev"]))
