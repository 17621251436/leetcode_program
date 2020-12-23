#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self , s ):
        # write code here
        stack=[]
        memo={'(':')','{':'}','[':']'}
        for i in s:
            if i in memo:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                node=stack.pop()
                if memo[node]==i:
                    pass
                else:
                    return False
        return True if len(stack)==0 else False