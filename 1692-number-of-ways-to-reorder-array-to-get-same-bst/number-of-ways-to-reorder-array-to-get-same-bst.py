from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def solve(arr):
            if len(arr) <= 2:
                return 1

            left = [x for x in arr[1:] if x < arr[0]]
            right = [x for x in arr[1:] if x > arr[0]]

            from math import comb
            ways = comb(len(arr) - 1, len(left))

            return (ways * solve(left) * solve(right)) % MOD

        return (solve(nums) - 1) % MOD