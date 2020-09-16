# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 翻转首尾链表
        def reverse(head, tail):
            prev = tail.next
            p = head
            while prev != tail:
                nex = p.next
                p.next = prev
                prev = p
                p = nex
            return tail, head

        hair = ListNode(None)
        hair.next = head
        pre = hair
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next
