#给你一个链表数组，每个链表都已经按升序排列。

#请你将所有链表合并到一个升序链表中，返回合并后的链表。


#Definition for singly-linked list.
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

        # tmp=[]
        # for i in range(len(lists)):
        #     p=lists[i]
        #     while p:
        #         tmp.append(p.val)
        #         p=p.next
        # tmp.sort()

        # res=ListNode(None)
        # node=res
        # for i in range(len(tmp)):
        #     Node=ListNode(tmp[i])
        #     node.next=Node
        #     node=node.next
        # return res.next


        









