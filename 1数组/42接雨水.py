# 边界条件
# if not height: return 0
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        n = len(height)

        left,right=0,n-1
        maxleft,maxright=height[0],height[n-1]
        ans=0
        while left<=right:
            maxleft=max(maxleft,height[left])
            maxright=max(maxright,height[right])
            if maxleft<maxright:
                ans+=maxleft-height[left]
                left+=1
            else:
                ans+=maxright-height[right]
                right-=1
        return ans





