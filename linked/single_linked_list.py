# coding=utf8
"""
@Author: Changye Yang
@Date: 2023/6/29 16:37
单链表
"""


class SingleNode:
    """单链表节点"""

    def __init__(self, item):
        self.item = item
        self.next: SingleNode | None = None


class SingleLinkList:
    def __init__(self):
        self._head: SingleNode | None = None

    def is_empty(self):
        return self._head == None

    def length(self):
        """链表长度"""
        # cur指向链表头节点
        cur = self._head
        count = 0
        # 尾节点指向None， 当未达到尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

        print("结束")

    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item的node节点
        node = SingleNode(item)
        # 将节点的链接域指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node

    def append(self, item):

        """尾部插入元素"""
        # 初始化节点
        node = SingleNode(item)
        # 判断链表是否为空
        if self.is_empty():
            # 如果链表为空，将初始化节点赋值头结点
            self._head = node
        else:
            # 如果链表不为空，循环至最后一个节点，将最后一个节点的next指向需要尾部插入的节点
            cur = self._head
            while cur != None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        """指定位置添加元素"""
        # 若指定位置index位于第一个元素之前。则执行头部插入
        if index <= 0:
            self.add(item)
        # 若指定位置超过链表尾部， 则执行尾部插入
        elif index > self.length() - 1:
            self.append(item)
        # 找到指定位置
        else:
            # pre用来指向指定位置的前一个位置index-1，初始从头节点开始移动到指定位置
            node = SingleNode(item)
            count = 0
            pre = self._head
            while count < (index - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 没找到指定元素
            if cur.item != item:
                pre = cur
                cur = cur.next
            # 找到指定元素
            else:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head.next = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置后的一个
                    pre.next = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next

        return False
