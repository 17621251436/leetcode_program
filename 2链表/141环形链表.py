# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        while head.next and head.val :
            head.val=None
            head=head.next
        if not head.next :
            return False
        return True

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

##快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast=head
        slow=head
        while fast:
            if  fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next
            else:
                return False
            if slow==fast:
                return True
        return False

##集合set
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur=set()
        while head:
            if head  in cur:
                return True
            else:
                cur.add(head)
            head=head.next
        return False
