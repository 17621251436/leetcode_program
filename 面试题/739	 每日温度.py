class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        tmp=[]
        res=[0 for i in range(n)]
        for i in range(n):
            while len(tmp)!=0 and temperatures[i]>temperatures[tmp[-1]]:
                res[tmp[-1]]=i-tmp[-1]
                del tmp[-1]
            tmp.append(i)
        return res