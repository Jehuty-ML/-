class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class BilateralLinkList:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def getitem(self):
        cur = self.head
        while cur is not None:
            yield cur.data
            cur = cur.next

    def find(self, data):
        index = -1
        cur = self.head
        count = 0
        while cur is not None:
            if cur.data == data:
                index = count
                return index
            else:
                cur = cur.next
                count += 1
        return index



    def insert(self, index, data):
        if not isinstance(data, Node):
            data = Node(data)
        if self.isempty():
            self.head = data
        else:
            cur = self.head
            if index == 0:
                data.next = self.head
                self.head = data
                cur.prev = self.head
            elif index <= self.length()-1:
                for _ in range(index):
                    cur = cur.next
                data.next = cur
                cur.prev.next = data
                data.prev = cur.prev
                cur.prev = data
            else:
                self.append(data)

    def addfirst(self, data):
        self.insert(0, data)

    def append(self, data):
        if not isinstance(data, Node):
            data = Node(data)
        if self.isempty():
            self.head = data
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = data
            data.prev = cur

    def remove(self, data):
        '''
        1.判断表头，中间，表尾 2.表头还要判断是否只有一个数据 3.指针的移动
        :param data:
        :return:
        '''
        if self.isempty():
            return
        cur = self.head
        if cur.data == data:
            if cur.next is None:
                self.head = None
            else:
                self.head = None
                self.head.next.prev = None
        else:
            cur = cur.next
            flag = False
            while cur is not None:
                if cur.data == data:
                    flag = True
                    if cur.next is not None:
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
                        cur = cur.next
                    else:
                        cur.prev.next = None
                else:
                    cur = cur.next
            if not flag:
                raise Exception('%s is not in linklist' % data)

        # while cur is not None:
        #     if cur.data == data:
        #         if cur.next is not None:
        #             cur.prev.next = cur.next  #如果第一个就没有prev
        #         else:
        #             cur.prev.next = None
        #     else:
        #         cur = cur.next

    def pop(self, index):
        if self.isempty():
            return
        cur = self.head
        if index < 0 or index > self.length()-1:
            raise Exception('index must be from 0 to %s' % self.length()-1)
        for _ in range(index):
            cur = cur.next
        if cur.next is not None:
            cur.prev.next = cur.next
        else:
            cur.prev.next = None

    def removeall(self):
        self.head = None
        #head是空之后，prev和next就不存在，不能再赋值








if __name__ == '__main__':
    linklist = BilateralLinkList()
    print(linklist.isempty())

    for i in range(1, 5+1):
        linklist.append(i)

    print(linklist.length())

    linklist.addfirst(0)
    print(linklist.length())

    linklist.pop(3)
    print(linklist.length())

    index4 = linklist.remove(4)
    print(linklist.length())

    linklist.removeall()
    print(linklist.isempty())
