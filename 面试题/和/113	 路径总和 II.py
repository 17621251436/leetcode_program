# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return [[]]
        res=[]
        path=[]
        def dfs(root,tar):
            if not root:
                return []
            path.append(root.val)
            tar-=root.val
            if not root.left and not root.right:
                res.append(root.val)
            dfs(root.left,tar)
            dfs(root.right,tar)
            path.pop()
        dfs(root,sum)
        return res