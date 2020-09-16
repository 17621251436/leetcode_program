class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        def getLeftIdx(idx):
            """ 获取坐标idx节点的左子节点的坐标 """
            return 2 * idx + 1

        def getRightIdx(idx):
            """ 获取坐标idx节点的右子节点的坐标 """
            return 2 * idx + 2

        def swap(arr, idx1, idx2):
            """ 交换坐标idx1和idx2地值 """
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

        def buildMaxHeap(arr):
            """ 自第一个非叶子节点从右至左，从下至上构建大顶堆 """
            for idx in range(int(len(arr) / 2 - 1), -1, -1):
                adjustMaxHeap(arr, idx, len(arr))

        def adjustMaxHeap(arr, start, end):
            """ 对坐标[start, end]内的元素进行大顶堆调整"""
            largest = start
            while True:
                # 待调整父节点地左右子节点坐标
                left, right = getLeftIdx(start), getRightIdx(start)

                # 寻找父节点和其左右子节点中的最大值
                if left < end and arr[left] > arr[start]:
                    largest = left
                if right < end and arr[right] > arr[largest]:
                    largest = right

                # 如果父节点不是最大值，其某个子节点大于父节点
                if largest != start:
                    swap(arr, largest, start)  # 子节点与父节点进行值交换
                    start = largest  # 下一轮待调整的新父节点
                    continue  # 继续调整新父节点下的堆结构
                else:  # 该父节点是最大值
                    break  # 终止调整

        def maxHeapSort(arr):
            """ 大顶堆排序 """
            buildMaxHeap(arr)  # 由数组元素构造大顶堆
            # 对数组坐标[0, end]中的元素进行大顶堆排序
            for end in range(len(arr) - 1, -1, -1):
                swap(arr, 0, end)  # 交换堆顶元素至堆尾
                adjustMaxHeap(arr, 0, end)  # 重新调整全部堆元素构造新大顶堆

        maxHeapSort(arr)
        return arr[:k]

