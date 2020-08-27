#I. 按层打印： 题目要求的二叉树的 从上至下 打印（即按层打印），又称为二叉树的 广度优先搜索（BFS）。BFS 通常借助 队列 的先入先出特性来实现。
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res,queue=[],collections.deque()
        queue.append(root)
        while queue:

            tmp=[]
            for i in range(len(queue)):
                que=queue.popleft()
                tmp.append(que.val)
                if que.left: queue.append(que.left)
                if que.right: queue.append(que.right)
            res.append(tmp)
        return res