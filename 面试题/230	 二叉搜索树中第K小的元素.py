# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        self.k=k
        def dfs(root):
            if not root:
                return
            if self.k==0:
                return
            dfs(root.left)
            self.k-=1
            if self.k==0:
                self.res=root.val
            dfs(root.right)
        dfs(root)

        return self.res