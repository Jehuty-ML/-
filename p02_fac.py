#写代码要先写主程序和使用的代码，再编写前面的函数代码和子代码
class BigInt:  #用List存放每一位
    def __init__(self, value):
        self.digits = [value]

    def mul(self, n):
        addition = 0
        for i in range(len(self.digits)):
            digit = self.digits[i]
            value = digit * n + addition
            self.digits[i] = value %10
            addition = value // 10

        while addition >0:
            self.digits.append(addition%10)
            addition //= 10
        return

    def __repr__(self):
        result = ''
        for digit in reversed(self.digits):
            result += str(digit)
        return result

def fac(n):
    result = BigInt(1)
    for i in range(2, n+1):
        result.mul(i)
    return result

if __name__ == '__main__':
    for n in range(1,21):
        print(n, '! =', fac(n))  #fac(n)先用后定义


