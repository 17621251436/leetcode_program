#输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
















        # n=target//2+1
        # i=1
        # j=2
        # res=[]
        # while j<=n:
        #     Sum+=sum(list(range(i,j+1)))
        #     if Sum>target:
        #         i+=1
        #     elif Sum<target:
        #         j+=1
        #     else:
        #         res.append(list(range(i,j+1)))
        #         j+=1
        # return res