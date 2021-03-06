# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return  []
        res=[]
        def dfs(root,path):
            if not root:
                return path
            if not root.left and not root.right:
                res.append(path)
            path.append(root.val)
            choices=[]
            if  root.left:
                choices.append(root.left)
            if  root.right:
                choices.append(root.right)
            for choice in choices:
                dfs(choice,path)
                path.pop()
        dfs(root,[])
        return ['->'.join(map(str,i)) for i in res]
















    # res = []
    #
    # def back(root, path):
    #     if not root:
    #         return []
    #     path.append(root.val)
    #     if not root.left and not root.right:
    #         res.append(path[:])
    #
    #     choices = []
    #     if root.left:
    #         choices.append(root.left)
    #     if root.right:
    #         choices.append(root.right)
    #     for choice in choices:
    #         back(choice, path)
    #         path.pop()
    #
    # back(root, [])
    # return ["->".join(list(map(str, i))) for i in res]
    #
    #