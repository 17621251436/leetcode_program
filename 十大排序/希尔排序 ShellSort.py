def ShellSort(lst):
    def shellinsert(arr, d):
        n = len(arr)
        for i in range(d, n):
            j = i - d
            temp = arr[i]  # 记录要出入的数
            while (j >= 0 and arr[j] > temp):  # 从后向前，找打比其小的数的位置
                arr[j + d] = arr[j]  # 向后挪动
                j -= d
            if j != i - d:
                arr[j + d] = temp

    n = len(lst)
    if n <= 1:
        return lst
    d = n // 2
    while d >= 1:
        shellinsert(lst, d)
        d = d // 2
    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = ShellSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ') 