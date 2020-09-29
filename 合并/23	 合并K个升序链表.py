# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        cur=res=ListNode(None)
        tmp=[]
        for num in lists:
            while num:
                tmp.append(num.val)
                num=num.next
        tmp.sort()
        for num in tmp:
            res.next=ListNode(num)
            res=res.next
        return cur.next