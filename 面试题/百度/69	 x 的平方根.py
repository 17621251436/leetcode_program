class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        for i in range(1,x//2+1):
            if i*i<=x and (i+1)*(i+1)>x:
                return i