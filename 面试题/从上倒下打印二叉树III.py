## z字形打印树
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res,queue=[],collections.deque()

        queue.append(root)

        while queue:
            tmp = collections.deque()
            for _ in range(len(queue)):
                que=queue.popleft()
                if len(res)%2 ==1 :
                   tmp.appendleft(que.val)
                else:
                   tmp.append(que.val)
                if que.left:
                   queue.append(que.left)
                if que.right:
                   queue.append(que.right)
            res.append(list(tmp))
        return res