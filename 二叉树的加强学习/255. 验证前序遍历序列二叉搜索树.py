class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if not preorder:
            return True
        if preorder == sorted(preorder) or preorder == sorted(preorder)[::-1]:
            return True

        # 从左往右找第一个比它大的数
        index = -1
        for i, num in enumerate(preorder):
            if num > preorder[0]:
                index = i

                for j in range(index, len(preorder)):
                    if preorder[j] <= preorder[0]:
                        return False
                break
        if index < 0:
            return self.verifyPreorder(preorder[1:])
        else:
            return self.verifyPreorder(preorder[1:index]) and self.verifyPreorder(preorder[index:])