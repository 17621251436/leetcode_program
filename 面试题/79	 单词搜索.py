class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:  # word减少到0，找到合适的
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:  # 边界条件判断，首字母判断
            return False
        used = board[i][j]  # 记录当前字母，方便回溯时恢复
        board[i][j] = '#'  # 找到后修改当前字母，防止重复查找
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) or self.dfs(board, i, j + 1,
                                                                                                     word[
                                                                                                     1:]) or self.dfs(
            board, i, j - 1, word[1:])
        board[i][j] = used  # 恢复当前字母
        return res


