# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head,tail):
            pre=tail.next
            p=head
            while pre!=tail:
                tmp=p.next
                p.next=pre
                pre=p
                p=tmp
            return tail,head

        hair = ListNode(None)
        hair.next = head
        pre = hair
        while head:
            tail=pre
            for _ in range(k):
                tail=tail.next
                if not tail:
                    return hair.next
            tmp=tail.next
            head,tail=reverse(head,tail)
            pre.next=head
            tail.next=tmp
            pre=tail
            head=pre.next
        return hair.next

















    #     def reverse(head,tail):
    #         pre=tail.next
    #         p=head
    #         while pre!=tail:
    #             tmp=p.next
    #             p.next=pre
    #             pre=p
    #             p=tmp
    #         return tail,head
    #
    #     hair=ListNode(None)
    #     hair.next=head
    #     pre=hair
    #     while head:
    #         tail=pre
    #         for i in range(k):
    #             tail=tail.next
    #             if not  tail:
    #                 return hair.next
    #         tmp=tail.next
    #         head,tail=reverse(head,tail)
    #
    #         pre.next =head
    #         tail.next=tmp
    #         pre=tail
    #         head=tail.next
    #     return hair.next
    #
    #
    #