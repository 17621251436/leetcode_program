# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = cur = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next
        node.next = l1 if l1 else l2
        return cur.next

        # node=cur=ListNode(None)
        # while l1 and  l2:
        #     if l1.val<l2.val:
        #         node.next,l1=l1,l1.next
        #     else:
        #         node.next,l2=l2,l2.next
        #     node=node.next
        # node.next=l1 if l1 else l2
        # return cur.next