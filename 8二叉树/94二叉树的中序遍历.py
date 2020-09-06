class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def inorderTraverse(self, root:TreeNode) ->list[int]:

        ##递归
        if not root:
            return []
        res=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res
       ## 非递归，stack 左根右
        if not root:
            return []
        cur,stack,res=root,[],[]
        while cur or stack:
            while cur:
               
                stack.append(cur)
                cur=cur.left
            tmp=stack.pop()
            res.append(tmp.val)
            cur=tmp.right
        return res
            


if __name__ == "__main__":
    test=Solution()
    print(test.inorderTraverse([1,null,2,3]))
    
    