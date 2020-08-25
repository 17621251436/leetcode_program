# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p=ListNode(0)
        p.next=head
        ptr=p
        while ptr is not None and ptr.next is not None:
            if ptr.next.val == val:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return p.next


        return  head