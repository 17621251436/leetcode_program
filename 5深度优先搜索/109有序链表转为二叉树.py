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

            if not head:
                return head
            pre, slow, fast = None, head, head

            while fast and fast.next:
                fast = fast.next.next
                pre = slow
                slow = slow.next
            if pre:
                pre.next = None
            node = TreeNode(slow.val)
            if slow == fast:
                return node
            node.left = self.sortedListToBST(head)
            node.right = self.sortedListToBST(slow.next)
            return node