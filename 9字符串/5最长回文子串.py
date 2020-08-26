#给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenth =len(s)
        dp=[[False]*lenth for _ in range(lenth) ]
        ans=""
        for l in range(lenth):
            for i in range(lenth):
                j=i+l
                if j>len(s):
                    break

                if l==0:
                    dp[i][j]=True

                elif l==1:
                    dp[i][j]=(s[i]==s[j])
                else:
                    dp[i][j]=(s[i]==s[j])and(dp[i-1][j-1)
                if dp[i][j] and l+1>len(ans):
                    ans=s[i:j+1]
        return ans