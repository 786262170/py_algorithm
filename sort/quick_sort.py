# coding=utf8
"""
快速排序

快速排序（英语：Quicksort），⼜称划分交换排序（partition-exchange sort），
通过⼀趟排序将要排序的数据分割成独⽴的两部分，其中⼀部分的 所有数据都⽐另外⼀部分的所有数据都要⼩，
然后再按此⽅法对这两部分数 据分别进⾏快速排序，整个排序过程可以递归进⾏，以此达到整个数据变成 有序序列。
步骤为：
1. 从数列中挑出⼀个元素，称为"基准"（pivot），
2. 重新排序数列，所有元素⽐基准值⼩的摆放在基准前⾯，所有元素⽐基准值⼤的摆在基准的后⾯（相同的数可以到任⼀边）。
   在这个分区结束 之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
3. 递归地（recursive）把⼩于基准值元素的⼦数列和⼤于基准值元素的⼦ 数列排序。
递归的最底部情形，是数列的⼤⼩是零或⼀，也就是永远都已经被排序好 了。虽然⼀直递归下去，
但是这个算法总会结束，因为在每次的迭代 （iteration）中，它⾄少会把⼀个元素摆到它最后的位置去。

 * 最优时间复杂度：O(nlogn)
 * 最坏时间复杂度：O(n )
 * 稳定性：不稳定
"""


def quick_sort(alist, start, end):
    """快速排序"""
    # 递归退出的条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左👈🏻向右👉🏻移动的游标
    low = start

    # high为序列右边的由右👉🏻向左👈🏻移动的游标
    high = end

    while low < high:
        # 如果low与high未重合， 且high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1

        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合， 且low指向的元素不比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    # 退出循环后， low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)

    return alist


if __name__ == '__main__':
    data = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    import timeit

    start = timeit.default_timer()
    res = quick_sort(data, 0, len(data) - 1)
    print("运行耗时:", timeit.default_timer() - start)
    print(res)
