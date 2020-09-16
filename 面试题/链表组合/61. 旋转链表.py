# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k<=0:
           return head
        length,cur=1,head
        ##形成闭环
        while cur.next is not None:
            length+=1
            cur=cur.next
        cur.next=head

        for _ in range(length-k%length):
            cur=cur.next
        head,cur.next=cur.next,None
        return head