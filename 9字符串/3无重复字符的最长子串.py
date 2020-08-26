class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack=[]
        maxdepth=0
        for i in s:
            while i in stack:
                stack.pop(0)
            stack.append(i)
            maxdepth = max(len(stack),maxdepth)
        return maxdepth



##重复的最长子串 返回最长子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict={}
        maxNum=0
        alpha=0
        for i in s:
            dict[i]=dict.get(i,0)+1
            maxNum=max(maxNum,dict[i])
        for i,v in dict.items():
            if maxNum==v:
                alpha=i
        st=""
        for _ in range(maxNum):
            st+=alpha
        return st

