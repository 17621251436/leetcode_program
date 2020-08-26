class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root :
            return 0
        self.ans=0
        self.deep(root,0)
        return self.ans
    def deep(self,node,level):
        if not node:
            return
        if self.ans<level+1:  ##左为5 ans=5  右为6，遍历deep的时候，不动
            self.ans=level+1
        self.deep(node.left,level+1)
        self.deep(node.right,level+1)

import collections
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue =collections.deque()
        queue.append(root)
        ans=0
        while queue:
            ans+=1
            for _ in range(len(queue)):  #层次遍历
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

