# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queueP = deque([p])
        queueQ = deque([q])

        while queueP and queueQ:
            parentP = queueP.popleft()
            parentQ = queueQ.popleft()

            if parentP is None and parentQ is None:
                continue

            if parentP is None or parentQ is None:
                return False
            
            if parentP.val != parentQ.val:
                return False
            
            queueP.append(parentP.left)
            queueP.append(parentP.right)
            queueQ.append(parentQ.left)
            queueQ.append(parentQ.right)
        
        return True
