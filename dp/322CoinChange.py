from typing import *


class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     dp = [amount + 1] * (amount + 1)
    #     dp[0] = 0

    #     for a in range(1, amount + 1):
    #         for c in coins:
    #             if a - c >= 0:
    #                 dp[a] = min(dp[a], 1 + dp[a - c])
    #     return dp[amount] if dp[amount] != amount + 1 else -1
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(amount, depth):
            print("  " * depth, f"Calling helper with amount={amount}")
            if amount == 0:
                print("  " * depth, "Amount is 0, returning 0")
                return 0
            if amount < 0:
                print("  " * depth, "Amount is negative, returning inf")
                return float('inf')

            min_coin = float('inf')
            for coin in coins:
                print("  " * depth, f"Exploring coin={coin}")
                ans = helper(amount - coin, depth + 1)
                if ans != float('inf'):
                    min_coin = min(min_coin, 1 + ans)
                print("  " * depth, f"Min coin after coin={coin}: {min_coin}")

            print("  " * depth, f"Returning min_coin: {min_coin}")
            return min_coin

        print("Recursion calls:")
        result = helper(amount, 0)
        return result if result != float('inf') else -1

sol = Solution()
print(sol.coinChange([1, 2, 5], 11))
