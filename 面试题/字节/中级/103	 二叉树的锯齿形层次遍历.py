# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue= collections.deque()
        queue.append(root)
        res=[]
        level=0
        while queue:
            level+=1
            ans=collections.deque()
            for _ in range(len(queue)):
                tmp=queue.popleft()
                if level%2:
                    ans.append(tmp.val)
                else:
                    ans.appendleft(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
                res.append(list(ans))
        return res


