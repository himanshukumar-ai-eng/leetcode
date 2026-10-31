from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or dp[i][j] == 0:
                    continue

                ways = dp[i][j]

                # Try moving right and down
                for dx, dy in [(0, 1), (1, 0)]:
                    x, y = i + dx, j + dy

                    # 0 = right, 1 = down
                    direction = 0 if dx == 0 else 1

                    while 0 <= x < m and 0 <= y < n and grid[x][y] == 1:

                        # Reflect and change direction
                        if direction == 0:
                            x += 1
                            direction = 1
                        else:
                            y += 1
                            direction = 0

                    if 0 <= x < m and 0 <= y < n:
                        dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]