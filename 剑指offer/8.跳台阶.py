class Solution:
    def jumpFloor(self, number):
        if n<0:
            return 0
        if n<=2:
            return n
        result=[1,2]
        for i in range(2,len(number)):
            result[i]=result[i-1]+result[i-2]

        return result[-1]
