class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        abmap={}
        for a in A:
            for b in B:
                abmap[a+b]=abmap.get(a+b,0)+1
        count=0
        for c in C:
            for d in D:
                M= (c+d)*(-1)
                if M in abmap:
                    count+=abmap[M]
        return count

