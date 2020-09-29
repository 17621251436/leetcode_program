# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
       


        if not pre:
            return None
        node=TreeNode(pre[0])
        if len(pre)==1:
            return node
        i=post.index(pre[1])
        node.left=self.constructFromPrePost(pre[1:i+2],post[:i+1])
        node.right=self.constructFromPrePost(pre[i+2:],post[i+1:-1])
        return node
        
