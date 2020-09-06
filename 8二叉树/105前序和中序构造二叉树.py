class Solution:
    def buildTree(self,preorder:TreeNode,inorder:TreeNode)->TreeNode:
        if not preorder and not inorder:
            return None
        root=TreeNode(preorder[0])
        ind=inorder.index[preorder[0]]
    
        root.left=self.buildTree(preorder[1:ind+1],inorder[:ind])
        root.right=self.buildTree(preorder[ind+1:],inorder[ind+1:])
        return root