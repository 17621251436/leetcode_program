# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        nums=[]
        p=head
        while p:
            nums.append(p.val)
            p=p.next
        i=0
        if len(nums)%2==0:
            while i<len(nums)-1:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                i=i+2
        else:
            while i<len(nums)-2:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                i=i+2

        res=ListNode(None)
        node=res
        for num in nums:
            Node=ListNode(num)
            node.next=Node
            node =node.next
        return res.next
