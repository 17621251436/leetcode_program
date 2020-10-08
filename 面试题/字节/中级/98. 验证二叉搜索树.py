# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ##中序遍历
        stack=[]
        cur=root
        res=float("-inf")
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left
            tmp=stack.pop()
            if tmp.val<=res:
                return False
            res=tmp.val
            cur=tmp.right

        return True