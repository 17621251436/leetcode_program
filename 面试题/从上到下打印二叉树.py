#从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue=collections.deque()
        queue.append(root)
        res=[]
        while queue:
            for i in range(len(queue)):
              que=queue.popleft()
              res.append(que.val)
              if que.left:
                  queue.append(que.left)
              if que.right:
                  queue.append(que.right)
        return res



