from typing import *


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res = []

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_array = nums[i: j + 1]
                res.append(sub_array)
        print(res)
        max_c = float("-inf")
        for r in res:
            if r[0] % 2 == 0:
                c = 0
                for i in range(len(r) - 1):
                    if r[i] % 2 != r[i + 1] % 2 and r[i] <= threshold:
                        c += 1
                        continue
                if c == len(r) - 1:
                    max_c = max(max_c, c + 1)
        return max_c

    def print_all_subarrays(self, arr):
        n = len(arr)

        for start in range(n):
            for end in range(start, n):
                subarray = arr[start:end+1]
                print(subarray)


sol = Solution()
print(sol.longestAlternatingSubarray(
    [2, 3, 4, 5], 4))
# print(sol.print_all_subarrays([1, 2, 3]))
