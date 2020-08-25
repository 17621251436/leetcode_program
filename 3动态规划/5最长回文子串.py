
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenth=len(s)
        dp=[[False]*lenth for _ in range(lenth)]
        ans=""
        for l in range(lenth):
            for i in range(lenth):
                j=i+l
                if j>=len(s):  ##防止溢出
                    break
                if l==0:
                    dp[i][j]=True
                elif l==1:
                    dp[i][j]=(s[i]==s[j])
                else:
                    dp[i][j]=(dp[i+1][j-1]) and (s[i]==s[j])
                if dp[i][j] and l+1>len(ans):
                    ans=s[i:j+1]
        return ans