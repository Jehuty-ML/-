'''
模仿c语言的内存精度限制，用链表实现求100阶乘的结果
'''


class Node(object):
    """单链表的结点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, item):
        self._head = Node(item)

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

    def mul(self, value):
        addition = 0
        cur = self._head
        for _ in range(self.length()):
            temp = cur.item * value + addition
            cur.item = temp % 10
            addition = temp // 10
            cur = cur.next

        while addition:
            self.append(addition % 10)
            addition //= 10

    def reverse(self):
        cur = self._head
        pre = None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def __repr__(self):
        result = ''
        self._head = self.reverse()
        # self.reverse()
        for i in self.items():
            result += str(i)
        return result


if __name__ == '__main__':
    #阶乘100
    result = SingleLinkList(1)
    for i in range(1, 100+1):
        result.mul(i)
    print(result)