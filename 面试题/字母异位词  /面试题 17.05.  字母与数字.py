class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        if not array:
            return []

        dp = [0] * len(array)
        dp[0] = 1 if 'A' <= array[0] <= "Z" or 'a' <= array[0] <= 'z' else -1  ###字母减去数字

        for i in range(1, len(array)):
            dp[i] = dp[i - 1] + 1 if 'A' <= array[i] <= "Z" or 'a' <= array[i] <= 'z' else dp[i - 1] - 1

        dic = {}
        dic[0] = -1
        for i in range(len(dp)):
            dic[dp[i]] = dic.get(dp[i], i)

        max_length = 0
        left = 0
        right = 0

        for i in range(len(dp)):
            if i - dic[dp[i]] > max_length:
                left = dic[dp[i]]
                right = i + 1
                max_length = right - left

        return array[left + 1:right]



