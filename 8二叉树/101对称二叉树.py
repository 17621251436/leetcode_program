def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res

 max_nums=0
        sumNum=0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
             if i==0:
                 max_nums=nums[i]
             sumNum+=nums[i]
             max_nums=max(max_nums,sumNum)
             if sumNum<0:
                 sumNum=0
        return max_nums