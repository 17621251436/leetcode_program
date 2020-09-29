# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

##删除倒数第n个
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp=p=q=head
        while p:
            if n>=1:
                n-=1
            else:
                tmp=q
                q=q.next
            p=p.next
        
        if p==head:
            return head.next
        tmp.next=q.next
        del q
        return head
            
    class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 
        
        #step1: 快指针先走n步
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next 

        #step2: 快慢指针同时走，直到fast指针到达尾部节点，此时slow到达倒数第N个节点的前一个节点
        while fast and fast.next:
            slow, fast = slow.next, fast.next 
        
        #step3: 删除节点，并重新连接
        slow.next = slow.next.next 
        return dummy.next 
