class Solution:
    def maxArea(self, height: List[int]) -> int:
      ##暴力算法
        res=0
        i=0
        j=len(height)-1
        while i<j:
            tmp=(j-i)*min(height[i],height[j])
            if tmp>res:
                res=tmp
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1

        return res