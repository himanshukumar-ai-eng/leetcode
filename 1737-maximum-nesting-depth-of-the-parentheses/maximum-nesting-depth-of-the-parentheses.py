class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        ans = 0

        for ch in s:
            if ch == '(':
                count += 1
                ans = max(ans, count)
            elif ch == ')':
                count -= 1

        return ans