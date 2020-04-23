class Array:
    def __init__(self, capability=10):
        self.capability = capability
        self.data = [None] * self.capability
        self.size = 0

    def isempty(self):
        return self.size == 0

    def append(self, data):
        self.data[self.size-1+1] = data
        self.size += 1

    def insert(self, index, data):
        for i in range(index, self.capability-1+1):
            self.data[i+1] = self.data[i]
        self.data[index] = data

    def addfirst(self, data):
        if self.size == self.capability:
            self.resize(self.capability*2)





class Solution:
    def threeSum(self, nums):
        result = []
        for i in range(len(nums)):
            num1 = nums[i]
            rest1 = nums[i+1:]
            for j in range(len(rest1)):
                num2 = rest1[j]
                rest2 = rest1[j+1:]
                for num3 in rest2:
                    if num1 + num2 + num3 == 0:
                        list1 = sorted([num1, num2, num3])
                        result.append(list1)
        return

if __name__ == '__main__':
    a = Solution()
    print(a.threeSum([-1, 0, 1, 2, -1, -4]))
