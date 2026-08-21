from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            # Try every non-empty subset of coins
            for mask in range(1, 1 << n):

                common = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        common = lcm(common, coins[i])

                        if common > x:
                            valid = False
                            break

                if not valid:
                    continue

                # Odd number of coins -> add
                if bits % 2 == 1:
                    total += x // common
                # Even number -> subtract
                else:
                    total -= x // common

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left