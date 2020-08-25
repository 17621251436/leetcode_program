##反转m到n间的链表
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre,cur=None,head

        while m>1:
            pre=cur
            cur=cur.next
            m=m-1
        con,tail=pre,cur

        #反转m-n间的链表
        for _ in range(m-n):
            third=cur.next
            cur.next=pre
            pre.next=cur
            cur=third
        if con:
            con.next=pre
        else:
            head=pre

        tail.next=cur
        return head