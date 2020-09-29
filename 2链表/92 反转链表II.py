##反转m到n间的链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        res=ListNode(None)
        res.next=head
        pre=res
        
        for _ in range(m-1):
             pre=pre.next

        cur=pre.next
        for _ in range(n-m):
             temp=cur.next
             cur.next=temp.next
             temp.next=pre.next
             pre.next= temp
        return res.next
