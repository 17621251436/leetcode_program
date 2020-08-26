# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res=[]
        def helper(node,level):
            if not node:
                return
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            helper(node.left,level+1)
            helper(node.right,level+1)
        helper(root,0)
        return res[::-1]

