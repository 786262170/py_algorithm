# coding=utf8
"""
@Author: Changye Yang
@Date: 2023/6/29 16:12
二分查找

⼆分查找⼜称折半查找，优点是⽐较次数少，查找速度快，平均性能好；
其缺点是要求待查表为有序表，且插⼊删除困难。
因此，折半查找⽅法适⽤于 不经常变动⽽查找频繁的有序列表。
⾸先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字⽐较，如果两者相等，则查找成功；
否则利⽤中间位置记录将表分成前、后两个⼦表，如果中间位置记录的关键字⼤于查找关键字，
则进⼀步a查找前⼀⼦表，否则进⼀步查找后⼀⼦表。重复以上过程，直到找到满⾜条件的记录，使查找成功，或直到⼦表不存在为 ⽌，此时查找不成功。

* 最优时间浮渣度：O(1)
* 最优时间浮渣度：O(logn)
"""


# 非递归实现
def binary_search(alist, item):
    """非递归-二分查找"""
    first = 0
    last = len(alist) - 1
    while first <= last:
        mid_point = int((first + last) / 2)
        if alist[mid_point] == item:
            print(f"刚好在中位数，mid:{mid_point}")
            return True
        elif alist[mid_point] > item:
            last = mid_point - 1
        else:
            first = mid_point + 1
    return False


def recursion_binary_search(alist, item):
    """递归-二分查找"""
    # 递归退出条件
    if len(alist) == 0:
        return False

    mid_point = len(alist) // 2
    if alist[mid_point] == item:
        print(f"刚好在中位数，mid:{mid_point}")
        return True
    elif alist[mid_point] > item:
        return recursion_binary_search(alist[:mid_point], item)
    else:
        return recursion_binary_search(alist[mid_point + 1:-1], item)


if __name__ == '__main__':
    data = [0, 1, 2, 8, 9, 13, 17, 19, 43, 2]
    recursion_binary_search(data, 17)
    # binary_search(data, 17)
