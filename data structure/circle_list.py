class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circlelist:
    def __init__(self):
        #引入哨兵节点
        self.head = Node(None)

    def isempty(self):
        return self.head.next is None

    def length(self):
        count = 0
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
            count += 1
        return count


    def insert(self, index, data):
        if not isinstance(data, Node):
            data = Node(data)
        if index < 0:
            raise Exception('index must bigger than 0!')
        elif index <= self.length():
            cur = self.head
            for _ in range(index):
                cur = cur.next
            data.next = cur.next
            cur.next = data
        else:
            real_index = index % self.length()
            self.insert(real_index, data)


    def addfirst(self, data):
        if not isinstance(data, Node):
            data = Node(data)
        self.insert(0, data)
        return

    def last(self):
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        last = cur
        return last

    def append(self, data):
        if not isinstance(data, Node):
            data = Node(data)
        if self.head.next is None:
            self.head.next = data
            data.next = self.head
        else:
            data.next = self.head
            self.last().next = data
        return

    def find(self, item):
        cur = self.head.next
        count = 0
        index = -1
        for _ in range(self.length()):
            if cur.data == item:
                index = count
            count += 1
            cur = cur.next
        return index

    def pop(self, index):
        if index < 0:
            raise Exception('can not be negative!')
        cur = self.head
        for _ in range(index):
            cur = cur.next
        data = cur.next.data
        cur.next = cur.next.next
        return data

    def remove(self, data):
        if self.find(data) == -1:
            raise Exception('%s not exist!' % data)
        else:
            index = self.find(data)
            self.pop(index)
        return index



    def removeall(self):
        if self.head.next is None:
            raise Exception('linklist has no Node!')
        else:
            self.head.next = None

    def gai(self, index, data):
        if not isinstance(data, Node):
            data = Node(data)
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        cur.data = data.data
        return

if __name__ == '__main__':
    linklist = Circlelist()
    print(linklist.isempty())

    for i in range(1, 5+1):
        linklist.append(i)

    print(linklist.length())

    linklist.addfirst(0)
    print(linklist.length())

    linklist.pop(3)
    print(linklist.length())

    index4 = linklist.remove(4)
    print('removeindex:%s' % index4, 'length:', linklist.length())

    linklist.removeall()
    print(linklist.isempty())








