#实现一个支持动态扩容的数组并完成其增删改查

class Array:
    def __init__(self, capability=10):
        self.capability = capability
        self._size = 0
        self._data = [None] * self.capability

    def __getitem__(self, item):
        return self.data[item]

    def length(self):
        """返回数组有效元素的个数"""
        return self._size

    def getCapability(self):
        """返回当前数组的容量"""
        return self.capability

    def isEmpty(self):
        return self._size == 0

    def insert(self, index, elem):
        if index < 0:
            print('index无效，请输入0到%s之间的数' % (self.capability))
        elif index > self.capability - 1:
            self.append(elem)
        elif self._size == self.capability:
            self.resize()  #扩容成两倍
        # 从尾部开始挪动元素，在index处腾出一个空间
        # 一定要注意在步长为负数的情况下，区间是左开右闭区间，即(index, self._size - 1]，所以是index-1，与正常的左闭右开区间是相反的！
        for i in range(self._size - 1, index - 1, -1):
            self._data[i+1] = self._data[i]
        self._data[index] = elem
        self._size += 1

    def resize(self, times=2):  #默认拓展成2倍容量
        self.capability *= times
        self._data += [None] * (times - 1)

        # private
        # def _resize(self, new_capacity):
        #     """
        #     数组容量放缩至new_capacity，私有成员函数
        #     :param new_capacity: 新的容量
        #     """
        #     new_arr = Arr(new_capacity)  # 建立一个新的数组new_arr，容量为new_capacity
        #     for i in range(self._size):
        #         new_arr.addLast(self._data[i])  # 将当前数组的元素按当前顺序全部移动到new_arr中
        #     self._capacity = new_capacity  # 数组容量变为new_capacity
        #     self._data = new_arr._data



    def append(self, elem):
        if self._size >= self.capability:
            self.resize()
        self._data[self._size-1+1] = elem
        self._size += 1

    def addfirst(self, elem):
        """
        想数组头部添加元素
        时间复杂度：O(n)
        :param elem: 所要添加的元素
        """
        self.insert(0, elem)  # 同理直接调用add方法

    def pop(self, index):
        if index < 0 or index > self._size-1:
            raise Exception('数组中仅有%s个元素' % self._size)
        ret = self._data[index]

        for i in range(index, self._size-1-1+1):  #-1:最后一位的index为size-1, -1：i只要遍历到倒数第二个 +1：左闭右开
            self._data[i] = self._data[i+1]
        self._data[self._size-1] = None
        self._size -= 1

        #还考虑缩减内存占用
        if self._size and self.capability / self._size >= 4:
            self.resize(0.5)
        return ret

    def remove(self, elem):
        if self.find(elem) == -1:
            raise Exception
        for i in range(0, self._size-1+1, 1):
            if self._data[i] == elem:
                self.pop(i)

    def removeall(self):
        self._data = [None] * 10
        self.capability = 10
        self._size = 0



    def gai(self, index, elem):
        if index < 0:
            raise Exception('index must be 0 or bigger!')
        if index >= self._size:
            self.append(elem)
        else:
            self._data[index] = elem

    def find(self, elem):
        count = 0
        index = -1
        for data in self._data:
            if data == elem:
                index = count
                return index
            count += 1
        return index

    def merge(self, other):
        if not isinstance(other, Array):
            raise Exception('%s must be Array' % other)
        for i in range(0, other._size-1+1, 1):
            self.append(other._data[i])

    def _gentestarray(self):
        for i in range(1, 6 + 1):
            self.append(i)

    def _myprint(self):
        for i in range(0, self._size-1+1):
            print(self._data[i], end='\t')
        print()
        print('size:', self._size, 'capability:', self.capability)



if __name__ == '__main__':
    linklist = Array()
    print(linklist.isEmpty())

    linklist._gentestarray()

    print(linklist.length())

    linklist.addfirst(0)
    print(linklist.length())

    linklist.pop(3)
    print(linklist.length())

    index4 = linklist.remove(4)
    print(linklist.length())

    # linklist.removeall()
    print(linklist.isEmpty())

    linklist2 = Array()
    linklist2._gentestarray()

    linklist.merge(linklist2)

    linklist._myprint()


