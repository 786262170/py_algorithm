# coding=utf8
"""
冒泡排序（英语：Bubble Sort）是⼀种简单的排序算法。
它重复地遍历要排序的数列，⼀次⽐较两个元素，如果他们的顺序错误就把他们交换过来。
遍历数列的⼯作是重复地进⾏直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越⼩的元素会经由交换慢慢“浮”到数列的 顶端。

冒泡排序算法的运作如下：
1、⽐较相邻的元素。如果第⼀个⽐第⼆个⼤（升序），就交换他们两个。
2、对每⼀对相邻元素作同样的⼯作，从开始第⼀对到结尾的最后⼀对。这步做完后，最后的元素会是最⼤的数。
3、针对所有的元素重复以上的步骤，除了最后⼀个。
4、持续每次对越来越少的元素重复上⾯的步骤，直到没有任何⼀对数字需要⽐较。

* 最优时间复杂度：O(n) （表示遍历⼀次发现没有任何可以交换的元素， 排序结束。）
* 最坏时间复杂度：O(n2)
* 稳定性：稳定
"""


def bubble_sort(alist: list):
    for j in range(len(alist) - 1, 0, -1):
        # j表示每次遍历需要比较的次数，逐渐减少
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist


if __name__ == '__main__':
    data = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    import timeit
    start = timeit.default_timer()
    res = bubble_sort(data)
    print("运行耗时:", timeit.default_timer() - start)
    print(data)
