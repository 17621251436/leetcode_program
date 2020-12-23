#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , str1 , str2 ):
        # write code here
        m,n=len(str1),len(str2)
        res,temp=0,''
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                if dp[i][j]>res:
                    temp=str1[i-dp[i][j]:i]
                    res=dp[i][j]
        return temp if temp else -1


#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
# class Solution:
#     def LCS(self, str1, str2):
#         # write code here
#         if len(str1) > len(str2):
#             str1, str2 = str2, str1
#
#         max_len, res = 0, ''
#
#         for i in range(len(str1)):
#             if str1[i - max_len: i + 1] in str2:
#                 res = str1[i - max_len: i + 1]
#                 max_len += 1
#
#         if not res:
#             return '-1'
#         else:
#             return res