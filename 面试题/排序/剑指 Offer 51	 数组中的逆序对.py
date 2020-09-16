class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(l=0, r=len(nums)):  # 左闭右开区间
            if r - l > 1:
                mid = (l + r) // 2
                mergeSort(l, mid)
                mergeSort(mid, r)
                i, j, tmp = l, mid, []
                while i < mid and j < r:
                    if nums[i] <= nums[j]:
                        tmp.append(nums[i])
                        i += 1
                    else:
                        tmp.append(nums[j])
                        j += 1
                        self.cnt += mid - i
                tmp.extend(nums[i:mid] if i < mid else nums[j:r])
                nums[l:r] = tmp

        self.cnt = 0
        mergeSort()
        return self.cnt
