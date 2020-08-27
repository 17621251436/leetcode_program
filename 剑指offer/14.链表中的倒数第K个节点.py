class Solution:
    def FindKthToTail(self, head, k):
        p=head
        q=head
        while k>=1:
            p=p.next
            k-=1
        while p:
            q=q.next
            p=p.next
        return q
