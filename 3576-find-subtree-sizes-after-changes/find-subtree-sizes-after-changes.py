
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Step 1: Build original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Step 2: Find new parents using DFS
        new_parent = parent[:]
        last = [-1] * 26

        stack = [(0, 0, -1)]

        while stack:
            node, state, old = stack.pop()
            c = ord(s[node]) - ord('a')

            if state == 0:
                old = last[c]

                if node != 0 and old != -1:
                    new_parent[node] = old

                last[c] = node

                stack.append((node, 1, old))

                for child in reversed(children[node]):
                    stack.append((child, 0, -1))

            else:
                last[c] = old

        # Step 3: Build final tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Step 4: Calculate subtree sizes
        ans = [1] * n
        stack = [(0, False)]

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))

                for child in new_children[node]:
                    stack.append((child, False))

            else:
                for child in new_children[node]:
                    ans[node] += ans[child]

        return ans
