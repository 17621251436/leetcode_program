# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
    ##109是有序的链表
        def midean(left,right):
            fast=slow=left
            while fast!=right and fast.next !=right:
                fast=fast.next.next
                slow=slow.next
            return slow


        def buildtree(left,right):
            if left == right:
                return None
            mid=midean(left,right)
            root=TreeNode(left,right)
            root.left=buildtree(left,mid)
            root.right=bulldtrr(mid.right)
            return root
        return buildtree(head,None)

        stack=[]
        while head:
            stack.append(head.val)
            head=head.next
        def buildtree(left,right):
            if left>right:
                return None
            mid(left+right+1)//2
            root=TreeNode(stack[mid])
            root.left=buildtree(left,mid-1)
            root.right=buildtree(mid+1,right)
            return root
        return  buildtree(0,len(stack)-1)



