def CountSort(ls):
    n = len(ls)
    num = max(ls)
    count = [0] * (num + 1)
    for i in range(0, n):
        count[ls[i]] += 1
    arr = []
    for i in range(0, num + 1):
        for j in range(0, count[i]):
            arr.append(i)
    return arr


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = CountSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')