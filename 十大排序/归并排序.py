class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        self.mergeSort(arr, 0, len(arr) - 1)
        return arr[:k]

    def mergeSort(self, arr, start, end):
        """ 通过递归对左右两边元素进行归并排序 """
        if start < end:
            mid = int((start + end) / 2)
            self.mergeSort(arr, start, mid)  # 对左半边的元素进行排序
            self.mergeSort(arr, mid + 1, end)  # 对右半边的元素进行排序
            self.mergeArray(arr, start, mid, end)  # 待左右两边元素有序后，进行合并操作

    def mergeArray(self, arr, start, mid, end):
        """ 将有序数组arr[start ~ mid]和arr[mid+1 ~ end]合并 """
        tmp = []  # 辅助数组，用于暂时存储排序后的元素
        p1, p2 = start, mid + 1  # 双指针：p1指向左半边的元素，p2指向右半边的元素
        while p1 <= mid and p2 <= end:  # 寻找较小的元素
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1
        if p1 <= mid:  # 若左半边还有剩余元素，将其直接添至辅助数组中
            tmp.extend(arr[p1:mid + 1])
        elif p2 <= end:  # 若右半边还有剩余元素，将其直接添至辅助数组中
            tmp.extend(arr[p2:end + 1])
        arr[start:end + 1] = tmp  # 将排序后的辅助数组赋值给原数组

