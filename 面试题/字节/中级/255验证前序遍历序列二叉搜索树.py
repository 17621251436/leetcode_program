class Solution(object):
    def verifyPreorder(self, preorder):
        if not preorder:
            return True

        if preorder==sorted(preorder) or preorder==sorted(preorder)[::-1]:
            return True

        index=-1
        ##搜索右边 根左右
        tmp=preorder[0]
        for i in  range(1,len(preorder)):
            if preorder[i]>tmp:
                index=i
                for j in range(index,len(preorder)):
                    if preorder[j]<tmp:
                        return False
                break
        if index<0:
            return self.verifyPreorder(preorder[1:])
        else:
            return self.verifyPreorder(preorder[1:index]) or self.verifyPreorder(preorder[index:])
