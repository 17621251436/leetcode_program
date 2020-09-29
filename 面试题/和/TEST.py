# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        def dfs(root):
            if not root:
                return []
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res

        cur,stack,res=root,[],[]
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur=cur.right
            tmp=stack.pop()
            cur=tmp.left
        return res[::-1]




