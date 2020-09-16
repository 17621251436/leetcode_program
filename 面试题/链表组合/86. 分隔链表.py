# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre = ListNode(None)
        res = pre
        back = ListNode(None)
        temp = back

        while head:

            if head.val < x:
                pre.next = head
                pre = pre.next
            else:
                back.next = head
                back = back.next
            head = head.next

        pre.next = temp.next
        back.next = None
        return res.next

