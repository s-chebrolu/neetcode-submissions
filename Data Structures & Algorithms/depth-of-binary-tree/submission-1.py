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

        return self.iterate(root, 0, 0)

    def iterate(self, node: Optional[TreeNode], depth: int, maxi: int) -> int:
        if node == None:
            return depth

        # self.iterate(node.left, depth + 1, maxi)
        # self.iterate(node.right, depth + 1, maxi)
        return max(self.iterate(node.left, depth + 1, maxi), self.iterate(node.right, depth + 1, maxi))
        # if maxi < depth:
        #     maxi = depth
        # return maxi

        