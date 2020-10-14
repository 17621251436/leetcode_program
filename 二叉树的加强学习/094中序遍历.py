class TreeNodo:
    def __init__(self,x):
        self.x=x
        self.left=None
        self.right=None
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        if not root:
            return []
        def dfs(root):
            if not root:
                return []
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res


        ###不遍历的写法

        res=[]
        if not root:
            return []
        stack,res,cur=[],[],root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left

            tmp=stack.pop()
            res.append(tmp.val)
            cur=tmp.right
        return res















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


