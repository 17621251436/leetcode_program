# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        res=ListNode(None)
        res.next=head
        pre=res
        for _ in range(m-1):
            pre=pre.next

        cur=pre.next
        for _ in range(n-m):
            temp=cur.next
            cur.next=temp.next
            temp.next=pre.next
            pre.next=temo
        return res.next


    if head is None or head.next is None or k <= 0:  # 特判
        return head

    # 1: 获取长度，且原头尾连接成环
    length, cur = 1, head
    while cur.next is not None:
        length += 1
        cur = cur.next
    cur.next = head  # 成环

    # 2: 原尾部节点指针游走 length - k % length 步, 到达新的尾部节点
    for _ in range(length - k % length):
        cur = cur.next

    # 3: 新的尾部与头部节点断开连接，返回新的头部节点
    head, cur.next = cur.next, None
    return head


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head  or not head.next or k<=0:
            return head

        lenth,cur=1,head
        while cur.next:
            lenth+=1
            cur=cur.next
        cur.next=head

        for _ in range(lenth-k%lenth):
            cur=cur.next
        head,cur.next=cur.next,None
        return head




