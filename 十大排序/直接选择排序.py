def direct_insert_sort(demo):
    print('排序前{}'.format(demo))
    demo = [0] + demo
    length = len(demo)
    for i in range(2, length):
        demo[0] = demo[i]  # 放置哨兵
        j = i - 1
        if demo[j] > demo[0]:
            while demo[j] > demo[0]:
                demo[j+1] = demo[j]
                j -= 1
            demo[j + 1] = demo[0]
        print('{}次:{}'.format(i, demo))
    demo = demo[1:]
    print("最终排序{}".format(demo))