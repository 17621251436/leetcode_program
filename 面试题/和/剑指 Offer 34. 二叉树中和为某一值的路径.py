class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:





        # res=[]
        # path=[]
        # if not root:
        #     return []
        # def dfs(root,tar):
        #     if not root :
        #         return  []
        #     path.append(int(root.val))
        #     tar-=root.val
        #     if tar==0 and  not root.left and not root.right:
        #         res.append(path)
        #     dfs(root.left,tar)
        #     dfs(root.right,tar)
        #     path.pop()
        # dfs(root,sum)
        # return res
