class Solution:
    def Fibonacci(self, n):
        if n<0:
            return 0
        if n==1 or n== 2:
            return n

        return  Fibonacci(n-1)+Fibonacci(n-2)


###################
        if n<0:
            return 0
        a=b=1
        for i in range(3,n+1):
            a,b=b,a+b
        return b

