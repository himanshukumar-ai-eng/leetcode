from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root, None)])

        while q:
            size = len(q)
            parent_x = None
            parent_y = None

            for i in range(size):
                node, parent = q.popleft()

                if node.val == x:
                    parent_x = parent

                if node.val == y:
                    parent_y = parent

                if node.left:
                    q.append((node.left, node))

                if node.right:
                    q.append((node.right, node))

            if parent_x is not None or parent_y is not None:
                return (parent_x is not None and
                        parent_y is not None and
                        parent_x != parent_y)

        return False