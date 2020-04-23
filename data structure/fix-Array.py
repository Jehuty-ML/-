class Array:
    def __init__(self, capability=10):
        self.size = 0
        self.data = [None] * capability
        self.capability = capability

    def isempty(self):
        return self.size == 0

    def length(self):
        return self.size

    def isfull(self):
        return self.size == self.capability

    def insert(self, index, data):
        if self.isfull():
            raise Exception('Array is full, cannot insert all more data')
        if index < 0 or index > self.capability-1:
            raise Exception('index must be from 0 to %s' % (self.capability-1))
        elif index > self.size-1:
            self.append(data)
        else:
            for i in range(self.size-1, index-1, -1):
                self.data[i+1] = self.data[i]
            self.data[index] = data
            self.size += 1

    def addfirst(self, data):
        self.insert(0, data)

    def append(self, data):
        if self.isfull():
            raise Exception('Array is full, cannot insert all more data')
        self.data[self.size-1+1] = data
        self.size += 1

    def pop(self, index):
        if self.isempty():
            raise Exception('Array is empty, cannot delete any data')
        if index < 0 or index > self.size - 1:
            raise Exception('Array has only {0} numbers, index must be from 0 to {0}'.format(self.size - 1))
        else:
            for i in range(index, self.size-1-1+1):
                self.data[i] = self.data[i+1]
            self.size -= 1

    def remove(self, data):
        if self.isempty():
            raise Exception('Array is empty, cannot delete all data')
        if self.find(data) == -1:
            raise Exception('%s is not in Array' % data)
        else:
            for i in range(self.find(data), self.size-1-1+1):
                self.data[i] = self.data[i+1]
            self.size -= 1

    def find(self, data):
        count = 0
        index = -1
        for i in range(self.size-1+1):
            if self.data[i] == data:
                index = count
                return index
            count += 1
        return index

    def removeall(self):
        self.size = 0
        self.data = [None] * self.capability

if __name__ == '__main__':
    linklist = Array()
    print(linklist.isempty())

    for i in range(1, 5+1):
        linklist.append(i)

    print(linklist.length())

    linklist.addfirst(0)
    print(linklist.length())

    linklist.pop(3)
    print(linklist.length())
    # linklist.pop(10)

    index4 = linklist.remove(4)
    print(linklist.length())

    linklist.removeall()
    print(linklist.isempty())