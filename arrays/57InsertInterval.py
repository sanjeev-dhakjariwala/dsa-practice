from typing import *


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals that come before the newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals with the newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval to the result
        result.append(newInterval)

        # Add all intervals that come after the newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


sol = Solution()
print(sol.insert([[1, 3], [6, 9]], [2, 5]))
