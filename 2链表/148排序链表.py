# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        tmp=[]
        res=ListNode(None)
        pre=res
        while head:
            tmp.append(head.val)
            head=head.next
        tmp.sort()
        for i in range(len(tmp)):
            temp=ListNode(tmp[i])
            pre.next=temp
            pre=pre.next
        return res.next