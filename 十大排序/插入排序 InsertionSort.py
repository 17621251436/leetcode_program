class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        gap = int(len(arr)/2)
        while gap >= 1:
            # 同直接插入排序
            for i in range(gap, len(arr)):  # 在每个子序列中，遍历所有无序元素（假设第一个元素有序）
                for j in range(i-gap, -1, -gap):  # 在该子序列中，对排在arr[i]前面的元素进行排序
                    if arr[j] > arr[j+gap]:
                        arr[j], arr[j+gap] = arr[j+gap], arr[j]
                    else:
                        break
            gap = int(gap/2)  # gap对折减半
        return arr[:k]

