# coding=utf8
"""
@Author: Changye Yang
@Date: 2023/06/29

选择排序（Selection sort）是⼀种简单直观的排序算法。它的⼯作原理如下:

⾸先在未排序序列中找到最⼩（⼤）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最⼩（⼤）元素，
然后放到已排 序序列的末尾。以此类推，直到所有元素均排序完毕。
选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。
选择排序每次交换⼀对元素，它们当中⾄少有⼀个将被移到其最终位置上，因此对n个元素的表进⾏排序总共进⾏⾄多n-1次交换。
在所有的完全依靠交换去移动元素的排序⽅法中，选择排序属于⾮常好的⼀种。

时间复杂度：
* 最优复杂度O(n^2)
* 最坏复杂度O(n^2)
* 稳定性：不稳定（考虑升序每次选择最大的情况）
"""


def select_sort(alist):
    num = len(alist)
    # 需要进行n-1次操作
    for i in range(num - 1):
        # 记录最小位置
        min_index = i
        for j in range(i + 1, num):
            if alist[j] < alist[min_index]:
                min_index = j

        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[min_index], alist[i] = alist[i], alist[min_index]
    return alist


if __name__ == '__main__':
    data = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    import timeit

    start = timeit.default_timer()
    res = select_sort(data)
    print("运行耗时:", timeit.default_timer() - start)
    print(res)
