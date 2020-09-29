class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def preOrder(self,root:TreeNode) -> list[int]:
        ##非递归
        if not root:
            return []
        cur,stack,res=[]
        cur=root
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur=cur.left
            tmp=stack.pop()
            cur=tmp.right
        return res




        ##递归

        if not root:
            return []
        res=[]
        def dfs(root):
            if not root:
                return 
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
            