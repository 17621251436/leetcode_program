# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        head=ListNode(None)
        res=head

        while l1 or l2 or carry>0:
            tmp=carry
            tmp+=l1.val if l1 else 0
            tmp+=l2.val if l2 else 0
            if l1: l1=l1.next
            if l2: l2=l2.next
            res.next=ListNode(tmp%10)
            res=res.next
            carry=tmp//10
        return head.next


