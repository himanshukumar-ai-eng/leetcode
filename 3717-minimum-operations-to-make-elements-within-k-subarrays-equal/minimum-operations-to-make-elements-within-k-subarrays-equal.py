from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        left = []
        right = []
        delayed = defaultdict(int)
        left_sum = 0
        right_sum = 0
        left_size = 0
        right_size = 0

        def prune(heap):
            while heap and delayed[heap[0] if heap == right else -heap[0]] > 0:
                val = heap[0] if heap == right else -heap[0]
                delayed[val] -= 1
                heapq.heappop(heap)

        def add(v):
            nonlocal left_sum, right_sum, left_size, right_size
            if not left or v <= -left[0]:
                heapq.heappush(left, -v)
                left_sum += v
                left_size += 1
            else:
                heapq.heappush(right, v)
                right_sum += v
                right_size += 1
            balance()

        def remove(v):
            nonlocal left_sum, right_sum, left_size, right_size
            delayed[v] += 1
            if v <= -left[0]:
                left_sum -= v
                left_size -= 1
                if -left[0] == v:
                    prune(left)
            else:
                right_sum -= v
                right_size -= 1
                if right and right[0] == v:
                    prune(right)
            balance()

        def balance():
            nonlocal left_sum, right_sum, left_size, right_size
            while left_size > right_size + 1:
                prune(left)
                v = -heapq.heappop(left)
                heapq.heappush(right, v)
                left_sum -= v
                right_sum += v
                left_size -= 1
                right_size += 1

            while left_size < right_size:
                prune(right)
                v = heapq.heappop(right)
                heapq.heappush(left, -v)
                right_sum -= v
                left_sum += v
                right_size -= 1
                left_size += 1

        costs = []
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                prune(left)
                median = -left[0]
                costs.append(median * left_size - left_sum +
                             right_sum - median * right_size)

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]

                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + costs[i - x]
                    )

        return dp[n][k]