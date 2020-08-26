class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def issim(node1,node2):
            if not node1 and not node2:
                return True

            if node1 and node2 and node1.val==node2.val:
                return True
            else:
                return False
        if not root:
            return True
        else:
            return issim(root.left,root.right) and issim(root.right,root.left)