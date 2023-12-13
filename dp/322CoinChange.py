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
    def coinChange(self, coins, amount):
        def recursive_helper(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')

            min_coins = float('inf')
            for coin in coins:
                subproblem = recursive_helper(amount - coin)
                if subproblem != float('inf'):
                    min_coins = min(min_coins, subproblem + 1)

            return min_coins

        result = recursive_helper(amount)
        return result if result != float('inf') else -1


sol = Solution()
print(sol.coinChange([1, 2, 5], 11))
