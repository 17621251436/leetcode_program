class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        def helper(tmp,j):
            if j==n:
                ans.append(tmp)
            for i in range(j,n):
                if s[j:i+1]!=s[j:i+1][::-1]:
                    continue
                helper(tmp+[s[j:i+1]],i+1)
        helper([],0)
        return ans
