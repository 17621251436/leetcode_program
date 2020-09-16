class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = 0
        r = len(nums) - 1
        self.cnt = 0
        def merge(l, r):
            if l == r:
                return [nums[l]]
            else:
                mid = (r - l) // 2 + l
                left = merge(l, mid)
                right = merge(mid + 1, r)
                i = j = 0
                ans = []
                while i < len(left) and j < len(right):
                    if left[i] <= right[j]:
                        ans.append(left[i])
                        i += 1
                    else:
                        self.cnt += len(left) - i
                        ans.append(right[j])
                        j += 1
                if i != len(left):
                    ans += left[i:]
                if j != len(right):
                    ans += right[j:]
                return ans
        merge(l, r)
        return self.cnt

