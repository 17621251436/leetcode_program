class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        for i in range(len(arr)):  # 遍历所有坐标
            min_idx = i  # 记录当前遍历中的最小值坐标
            for j in range(i, len(arr)):  # 在未排序元素中寻找最小值
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 交换最小值至待排序元素坐标
        return arr[:k]

