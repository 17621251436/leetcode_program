# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        tmp=[]
        if not  lists:
            return None
        for i in range(len(lists)):
            temp=lists[i]
            while temp:
                tmp.append(temp.val)
                temp=temp.next
        tmp.sort()
        pre=ListNode(None)
        res=pre
        for num in tmp:
            res.next=ListNode(num)
            res=res.next
        return pre.next


# tmp=[]
# if not lists:
#     return None
# for i in range(len(lists)):
#     temp=lists[i]
#     while temp:
#         tmp.append(temp.val)
#         temp=temp.next
# tmp.sort()
# pre=ListNode(None)
# res=pre
# for i in range(len(tmp)):
#     res.next=ListNode(tmp[i])
#     res=res.next
# return pre.next


import heapq
    heap=[]
    pre=cur=ListNode(None)
    for  num in lists:
        while num:
            heapq.heappush(heapq,num.val)
            num=num.next

    while heap:
        val=heapq.pop(heap)
        pre.next=listNode(val)
        pre=pre.next
    pre.next=None
    return cur.next


