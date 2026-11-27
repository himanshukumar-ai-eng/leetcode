
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        INF = -10**9

        dp = [INF] * (budget + 1)
        dp[0] = 0

        for f, p in items:

            # Number of free copies from buying this item first
            free = sum(x % f == 0 for x, price in items) - 1

            buy = [INF] * (budget + 1)

            for c in range(p, budget + 1):

                # First copy OR additional copy
                buy[c] = max(
                    dp[c - p] + free + 1,
                    buy[c - p] + 1
                )

            # Choose: skip this item or buy it
            dp = [
                max(dp[c], buy[c])
                for c in range(budget + 1)
            ]

        return max(dp)
