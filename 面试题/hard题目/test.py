class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        def dfs(root,sumlist):
            if not root:
                return 0
            sumlist=[num+root.val for num in sumlist]
            sumlist.append(root.val)
            count=0
            for num in sumlist:
                if num==sum:
                    count+=1
            return count+dfs(root.left,sumlist)+dfs(root.right,sumlist)
        return dfs(root,[])

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_num= float('-inf')
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.max_num=max(self.max_num,left+right+root.val)
            return max(0,max(left,right)+root.val)
        dfs(root)
        return self.max_num

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def dfs(root,path):
            if not root:
                return []
            path.append(root.val)
            if not root.left and not root.right:
                res.append(path[:])
            choices=[]
            if root.left:
                choices.append(root.left)
            if root.right:
                choices.append(root.right)
            for choice in choices:
                dfs(choice,path)
                path.pop()
        dfs(root,[])
        return ['->'.join(list(map(str,i)))for i in res]

class Solution:
    def trap(self, height: List[int]) -> int:
          # 边界条件
        if not height: return 0
        n = len(height)

        left,right = 0, n - 1  # 分别位于输入数组的两端
        maxleft,maxright = height[0],height[n - 1]
        ans = 0

        while left <= right:
            maxleft = max(height[left],maxleft)
            maxright = max(height[right],maxright)
            if maxleft < maxright:
                ans += maxleft - height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1

        return ans