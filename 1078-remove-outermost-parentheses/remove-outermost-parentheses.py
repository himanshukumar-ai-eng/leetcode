class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        ans = ""

        for ch in s:
            if ch == '(':
                if balance > 0:
                    ans += ch
                balance += 1

            else:
                balance -= 1
                if balance > 0:
                    ans += ch

        return ans