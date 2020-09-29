# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur=res=ListNode(None)

        while l1 and l2:
            if l1.val<l2.val:
                cur.next,l1=ListNode(l1.val),l1.next
            else:
                cur.next,l2=ListNode(l2.val),l2.next
            cur=cur.next
        cur.next=l1 if l1 else l2
        return res.next