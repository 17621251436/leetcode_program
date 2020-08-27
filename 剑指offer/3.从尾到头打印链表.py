class Solution:
    def printListFromTailToHead(self, listNode):
        tmp=[]
        p=listNode
        while p:
            tmp.append(p.val)
        return tmp[::-1]