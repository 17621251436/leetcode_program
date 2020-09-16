class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}  # 统计每一个单词出现的频率
        for i in words:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        dic = sorted(dic.items(), key=lambda item: (-item[1], item[0]))
        return [key for key, _ in dic[:k]]

