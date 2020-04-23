class Node(object):
    """单链表的结点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def find(self, item):
        """查找元素是否存在"""
        return item in list(self.items())

    def add(self, item):
        """向链表头部添加元素"""
        if not isinstance(item, Node):
            item = Node(item)
        if self._head is  None:
            self._head = None
        else:
            item.next = self._head
            self._head = item


    def append(self, item):
        """尾部添加元素，相比于双向链表，少了前向指针"""
        if not isinstance(item, Node):
            item = Node(item)
        if self._head is not None:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = item
        else:
            self._head = item



    def insert(self, index, item):
        """指定位置插入元素"""
        if not isinstance(item, Node):
            item = Node(item)
        if index <= 0:
            self.add(item)
        elif index > self.length() - 1:
            self.append(item)
        else:
            cur = self._head
            for _ in range(index-1):
                cur = cur.next
            item.next = cur.next
            cur.next = item

    def remove(self, item):
        if self.find(item):
            cur = self._head
            pre = None
            while cur is not None:
                if cur.item == item:
                    if not pre:  #如果第一个节点就是要删除的
                        self._head = cur.next
                    else:
                        pre.next = cur.next
                else:
                    pre = cur
                    cur = cur.next
        else:
            '%s is not in single link list' % item

    def find(self, item): #item在index
        if item in self.items():
            index_list = []
            index = 0
            cur = self._head
            for _ in range(self.length()):
                if cur.item == item:
                    index_list.append(index)
                cur = cur.next
                index += 1
            return index_list


if __name__ == '__main__':
    # link_list = SingleLinkList()
    # # 向链表尾部添加数据
    # for i in range(5):
    #     link_list.append(i)
    # # 向头部添加数据
    # link_list.add(6)
    # # 遍历链表数据
    # for i in link_list.items():
    #     print(i, end='\t')
    # # 链表数据插入数据
    # link_list.insert(3, 9)
    # print('\n', list(link_list.items()))
    # # 删除链表数据
    # link_list.remove(0)
    # # 查找链表数据
    # print(link_list.find(0))
    # print(link_list.find(4))
















# # 1。__init_(): initialize the node with the data
# # 2。self.data: the value stored in the node
# # 3。self.next: the reference pointer to the next node
# # 4。 has_value(): compare a value with the node value
#
# class Node:
#     def __init__(self, data):
#         "constructor to initiate this object"
#
#         # store data
#         self.data = data
#
#         # store reference (next item)
#         self.next = None
#         return
#
# class SingleLinkedList:
#     def __init__(self):
#         "constructor to initiate this object"
#
#         self.head = None
#         self.tail = None
#         return
#
#     def add(self, item):
#         if not isinstance(item, Node):
#             item = Node(item)
#
#         if self.head is None:
#             self.head = item
#         else:
#             self.tail.next = item
#
#         self.tail = item
#         return
#
# if __name__ == '__main__':
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     linklist = SingleLinkedList()
#
#