class Solution(object):
    def mergeTwoLists(self, l1, l2):
        cur=head=ListNode(None)
        while l1 or l2:
            if l1.val>l2.val:
                cur.next=l2
                l2=l2.next
            else:
                cur.next = l1
                l1 = l1.next

            cur=cur.next
        cur.next=l1 or l2

        return head.next
