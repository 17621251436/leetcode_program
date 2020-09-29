# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur=ListNode(None)
        cur.next=head
        pre=cur
        
        while head and head.next:
              first=head
              second=head.next
              pre.next=second
              first.next=second.next
              second.next=first
              pre=first
              head=first.next

        return cur.next
        

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while head and head.next:   #空节点或者单节点退出
            first = head
            second = head.next
            pre.next = second       #交换两节点
            first.next = second.next
            second.next = first

            pre = first             #继续遍历后续节点
            head = first.next
        return dummy.next
