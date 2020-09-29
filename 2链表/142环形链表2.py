# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        ##双指针
        
        fast=slow=head
        while True:
            if not (fast and fast.next): return 
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break

        fast=head
        while fast!=slow:
            fast=fast.next
            slow=slow.next
        return fast



        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
