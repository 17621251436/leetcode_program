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
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left

            tmp =stack.pop()
            if  tmp.val<=res:
                return False
            cur=tmp.right
            res=tmp.val
        return True