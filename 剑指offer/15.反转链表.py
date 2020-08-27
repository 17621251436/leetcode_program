class Solution(object):
    def reverseList(self, head):
        if not head:
            return  None

        p=head
        q=head.next
        while q:
            head.next=q.next
            q.next=p
            p=q
            q=head.next
        return p