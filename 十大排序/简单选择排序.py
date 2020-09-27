def SelectSort(ls):
    n = len(ls)
    if n <= 1:
        return ls
    for i in range(0, n - 1):
        minIndex = i
        for j in range(i + 1, n):  # 比较一遍，记录索引不交换
            if ls[j] < ls[minIndex]:
                minIndex = j
        if minIndex != i:  # 按索引交换
            (ls[minIndex], ls[i]) = (ls[i], ls[minIndex])
    return ls


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = SelectSort(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')