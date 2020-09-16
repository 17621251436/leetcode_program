# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        tmp = []
        while queue:
            temp = []
            for _ in range(len(queue)):
                res = queue.popleft()
                temp.append(res.val)
                if res.left:
                    queue.append(res.left)
                if res.right:
                    queue.append(res.right)
            tmp.append(temp)
        return tmp