# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p=l1=listNode(None)
        q=l2=ListNode(None)

        while head:
            if head.val<x:
                p.next=ListNode(head.val)
                p=p.next
            else:
                q.next=ListNode(head.val)
                q=q.next
            head=head.next
        p.next=l2.next
        return l1.next













        # p = l1 = ListNode(None)
        # q = l2 = ListNode(None)
        # while head:
        #     if head.val < x:
        #         l1.next = ListNode(head.val)
        #         l1 = l1.next
        #     else:
        #         l2.next = ListNode(head.val)
        #         l2 = l2.next
        #     head = head.next
        # l1.next = q.next
        # return p.next
