# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if  not root:
            return []
        queue=collections.deque()
        queue.append(root)
        res=[]
        level=0
        while queue:
            tmp=collections.deque()
            level+=1
            for _ in range(len(queue)):

                temp=queue.popleft()
                if level%2:
                    tmp.append(temp.val)
                else:
                    tmp.appendleft(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            res.append(list(tmp))
        return res