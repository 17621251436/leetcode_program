# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        cur = stack.pop(0)
        while stack:
            cur.next = stack.pop()
            cur = cur.next
            if stack:
                cur.next = stack.pop(0)
                cur = cur.next
        cur.next = None

