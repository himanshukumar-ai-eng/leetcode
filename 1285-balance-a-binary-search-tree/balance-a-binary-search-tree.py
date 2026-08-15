class Solution:
    def inorder(self, root, nodes):
        if root is None:
            return

        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)

    def buildBalancedTree(self, nodes, start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        root = nodes[mid]

        root.left = self.buildBalancedTree(nodes, start, mid - 1)
        root.right = self.buildBalancedTree(nodes, mid + 1, end)

        return root

    def balanceBST(self, root):
        nodes = []

        self.inorder(root, nodes)

        return self.buildBalancedTree(nodes, 0, len(nodes) - 1)