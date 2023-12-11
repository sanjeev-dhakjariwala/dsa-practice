
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        num = abs(x)
        while x > 0:
            r = num % 10
            rev = rev * 10 + r
            x = x // 10

        return -rev if x < 0 else rev
    
sol = Solution()
print(sol.reverse(123))