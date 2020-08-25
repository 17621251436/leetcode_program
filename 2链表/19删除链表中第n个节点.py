# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p=head
        q=head
        r=head
        i=0

        while p is not None:
            if i<n:
                i=i+1
            else:
                r=q
                q=q.next
            p=p.next

        if p==head:
            return head.next

        r.next=q.next
        del q
        return head
