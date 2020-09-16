class Solution:
    def longestWord(self, words: List[str]) -> str:
        def f(word):
            for i in range(len(word)):
                left = word[:i]
                right = word[i:]
                if left in words:  # 如果单词的左边是组合中的一个单词，则继续看右边
                    if right in words:
                        return True
                    elif f(right):  # 如果单词的右边是其他单词的组合，则返回 ture。否则继续寻找下一种划分。
                        return True
                    else:
                        continue
                else:
                    continue  # 如果单词的左边不是组合中的一个单词，则进行下一种划分。
            return False  # 如果不存在任何正确的划分，返回 false。
        res = ''
        for word in words:
            if f(word):
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):
                    res = min(res, word)
        return res