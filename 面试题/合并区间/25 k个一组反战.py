# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head, tail):
            prev = tail.next
            p = head
            while prev != tail:
                tmp = p.next
                p.next = prev
                prev = p
                p = tmp
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
            head = tail.next
            pre = tail
        return hair.next

        # def reverse( head, tail):
        #     prev = tail.next
        #     p = head
        #     while prev != tail:
        #         nex = p.next
        #         p.next = prev
        #         prev = p
        #         p = nex
        #     return tail, head

        # hair = ListNode(0)
        # hair.next = head
        # pre = hair

        # while head:
        #     tail = pre
        #     # 查看剩余部分长度是否大于等于 k
        #     for i in range(k):
        #         tail = tail.next
        #         if not tail:
        #             return hair.next
        #     nex = tail.next
        #     head, tail = reverse(head, tail)
        #     # 把子链表重新接回原链表
        #     pre.next = head
        #     tail.next = nex
        #     pre = tail
        #     head = tail.next

        # return hair.next