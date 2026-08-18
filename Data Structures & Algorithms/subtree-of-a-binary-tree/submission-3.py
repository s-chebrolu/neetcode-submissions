# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        if root is None:
            return False

        rootStack = [root]
        while rootStack:
            parentRoot = rootStack.pop()

            if parentRoot == None:
                continue

            if parentRoot.val == subRoot.val:
                rootCheck = [parentRoot]
                subCheck = [subRoot]
                same = True
                while rootCheck or subCheck:
                    groot = rootCheck.pop()
                    subgroot = subCheck.pop()

                    if groot == None and subgroot == None:
                        continue
                    
                    if groot == None or subgroot == None:
                        same = False
                        break

                    if groot.val != subgroot.val:
                        same = False
                        break

                    rootCheck.append(groot.left)
                    subCheck.append(subgroot.left)
                    rootCheck.append(groot.right)
                    subCheck.append(subgroot.right)
                if same:
                    return True
            rootStack.append(parentRoot.left)
            rootStack.append(parentRoot.right)

        return False
        