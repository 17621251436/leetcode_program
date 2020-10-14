class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def postOrder(self,root:TreeNode)->list[int]:
        ##递归
        if not root:
            return  []
        stack,res,cur=[],[],root
        res=[]
        while stack or cur:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur=cur.right
            tmp=stack.pop()
            cur=tmp.left
        return res[::-1]


        # if not root:
        #     return []
        # res=[]
        # dfs(root):
        #    if not root:
        #        return
        #     dfs(root.left)
        #     dfs(root.right)
        #     res.append(root.val)
        # dfs(root)
        # return res
        #
        # ##非递归 ：前序遍历 根左右（根右左）反序列 左右根
        #
        # if not root:
        #     return []
        # res=[]
        # cur=root
        # stack=[]
        # while stack or cur:
        #     while cur:
        #
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur=cur.right
        #     tmp=stack.pop()
            cur=tmp.left
        return res[::-1]
