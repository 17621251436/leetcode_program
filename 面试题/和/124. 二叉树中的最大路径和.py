# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_num= float("-inf")
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.max_num=max(self.max_num,left+right+root.val)
            return max(0,max(left,right)+root.val)
        dfs(root)
        return self.max_num