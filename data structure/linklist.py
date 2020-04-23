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
        item.next = self._head
        self._head = item
        return

    def append(self, item):
        """尾部添加元素"""
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

    def iscircle(self):
        temp_list = []
        cur = self._head
        while cur.next is not None:
            if cur.next in temp_list:
                return True
            temp_list.append(cur)
            cur = cur.next
        return False

    def last(self):
        cur = self._head
        while cur.next:
            cur = cur.next
        last = cur
        return last

    def merge(self, other):
        if not isinstance(other, SingleLinkList):
            raise Exception('the other one must be single link-list')
        self.last().next = other._head
        return self._head

    def getitem(self):
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def getmid(self):
        fast = self._head
        slow = self._head
        while fast.next is not None:
            slow = slow.next
            if fast.next.next is not None:
                fast = fast.next.next
            else:
                fast = fast.next
                return slow
        return slow

    def reverse(self):
        pass

if __name__ == '__main__':
    linklist = SingleLinkList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    linklist._head = node1
    node1.next = node2
    node2.next = node3
    # node3.next = node1

    print(linklist._head.item)


    # 链表中环的检测
    print(linklist.iscircle())



#
# 两个有序的链表合并

    linklist2 = SingleLinkList()
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    linklist2._head = node4
    node4.next = node5
    node5.next = node6
    print(linklist2.iscircle())

    linklist.merge(linklist2)
    for item in linklist.getitem():
        print(item, end=' ')
#
# 删除链表倒数第 n 个结点


#
# 求链表的中间结点
    print('\n', linklist.getmid().item)