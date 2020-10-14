# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur=ListNode(None)
        cur.next=head
        pre=cur
        
        while head and head.next:
              first=head
              second=head.next
              pre.next=second
              first.next=second.next
              second.next=first
              pre=first
              head=first.next

        return cur.next

        cur=ListNode(None)
        cur.next=head
        pre=cur
        while head and head.next:
            first=head
            second=head.next
            pre.next=second
            first.next=second.next
            second.next=first
            pre=first
            head=first.next
        return cur.next
















        








