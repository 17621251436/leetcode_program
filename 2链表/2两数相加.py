# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        nums1=""
        nums2=""
        while l1 is not None:
            nums1+=str(l1.val)
            l1=l1.next
        while l2 is not None:
            nums2+=str(l2.val)
            l2=l2.val

        sumNum=str(int(nums1[::-1])+int(nums2[::-1]))[::-1]
        head=listNode(sumNum[0])
        ptr=head

        for i in range(1,len(sumNum)):
            node=listNode(sumNum[i])
            ptr.next=node
            ptr=ptr.next
        return head
