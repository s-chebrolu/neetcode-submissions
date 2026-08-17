# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        return self.iterate(root, 0)

    def iterate(self, node: Optional[TreeNode], depth: int) -> int:
        if node == None:
            return depth

        return max(self.iterate(node.left, depth + 1), self.iterate(node.right, depth + 1))

        