class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            small = self.myPow(x, n + 1)
            return 1 / x * small
        if n == 1:
            return x

        return x * self.myPow(x, n - 1)

sol = Solution()
print(sol.myPow(2, -2))