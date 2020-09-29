# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur=res=ListNode(None)
        while l1 and l2:
            if l1.val>l2.val:
                cur.next,l2=ListNode(l2.val),l2.next
            else:
                cur.next,l1=ListNode(l1.val),l1.next
            cur=cur.next
        
        cur.next=l1 if l1 else l2
        return res.next


   # res=ListNode(None)
        # node=res
        # while l1 and  l2:
        #     if l1.val<l2.val:
        #         node.next,l1=l1,l1.next
        #     else:
        #         node.next,l2=l2,l2.next
        #     node=node.next
        # if l1:
        #     node.next=l1
        # else:
        #     node.next=l2
        # return res.next


      


        