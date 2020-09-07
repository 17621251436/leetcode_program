class TreeNodo:
    def __init__(self,x):
        self.x=x
        self.left=None
        self.right=None
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ##递归：
        if not root:
            return 0
        res=[]
        def dfs(root):

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

       ##遍历
        res=[]
        stack=[]
        cur=root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left

            tmp=stack.pop()
            res.append(tmp.val)
            cur=tmp.right
        return res


