class Solution:
    def jumpFloorII(self, number):
        if number <= 0:  return 0
        if number == 1:  return 1
        if number == 2:  return 2
        result=[1,2]
        for i in range(2,len(number)):
            result[i]=2*result[i-1]
        return result[-1]