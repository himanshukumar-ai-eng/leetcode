class Solution:
    def removeInvalidParentheses(self, s: str):
        def isValid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = {s}
        found = False
        ans = []

        while queue:
            curr = queue.pop(0)

            if isValid(curr):
                ans.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue

                new_str = curr[:i] + curr[i+1:]

                if new_str not in visited:
                    visited.add(new_str)
                    queue.append(new_str)

        return ans