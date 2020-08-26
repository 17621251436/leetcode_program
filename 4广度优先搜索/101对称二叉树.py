# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def issim(node1,node2) :
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val == node2.val:
                return issim(node1.left,node2.right) and issim(node1.right,node2.left)
            else:
                return False
        if not root:
            return True
        else:
            return issim(root.left,root.right)
