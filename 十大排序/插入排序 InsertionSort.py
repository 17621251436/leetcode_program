def InsertSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1, n):
        j = i
        target=lst[i]
        while target<lst[j-1] and j>=0:
            lst[j]=lst[j+1]
            j-=1
        lst[j]=target
     lst[i] =target  # 每次循环的一个待插入的数

return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = InsertSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
