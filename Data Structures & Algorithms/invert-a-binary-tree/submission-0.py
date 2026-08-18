# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        self.iterate(root)
        return root


    def iterate(self, node: Optional[TreeNode]) -> None:
        if node == None:
            return
        self.iterate(node.left)
        self.iterate(node.right)
        temp = node.right
        node.right = node.left
        node.left = temp