# coding=utf8
"""
@Author: Changye Yang
@Date: 2023/6/29 16:37
双端链表
"""


class Node:
    """双向链表节点"""

    def __init__(self, item):
        self.item = item
        self.next: Node | None = None
        self.prev: Node | None = None


class DoubleLinkList:
    def __init__(self):
        self._head: Node | None = None

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
        node = Node(item)
        if self.is_empty() == False:
            # 将node的next指向_head头结点
            node.next = self._head
            # 将头节点_head的prev指向node节点
            self._head.prev = node
        # 将链表的头_head指向新节点
        self._head = node

    def append(self, item):

        """尾部插入元素"""
        # 初始化节点
        node = Node(item)
        # 判断链表是否为空
        if self.is_empty():
            # 如果链表为空，将初始化节点赋值头结点
            self._head = node
        else:
            # 如果链表不为空，循环至最后一个节点，将最后一个节点的next指向需要尾部插入的节点
            cur = self._head
            while cur != None:
                cur = cur.next
            # 将尾节点cur的next指向node节点
            cur.next = node
            # 将 node节点的prev指向cur
            node.prev = cur

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
            node = Node(item)
            count = 0
            pre = self._head
            while count < (index - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.prev = pre
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next.prev = node
            pre.next = node.next

    def remove(self, item):
        """删除节点"""
        cur = self._head
        while cur != None:
            # 没找到指定元素
            if cur.item != item:
                cur = cur.next
            # 找到指定元素
            else:
                # 判断当前节点是否为头结点
                if cur == self._head:
                    # 将头指针指向头节点的后一个节点
                    self._head.next = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    # 将删除位置前一个节点的next指向删除位置后的一个
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next

        return False
