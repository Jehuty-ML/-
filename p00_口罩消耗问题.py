'''
每次出门买口罩消耗库存1只，限购3只每次，买到了多2只，买不到亏1只，现在原库存10只，出门10次后剩余12只，问多少次买到了
'''
import random

def get_mask(m, n=10):  #出门10次
    x = 10 #初始口罩数
    x = x + 2 * m - (10 - m)
    return x


if __name__ == '__main__':
    for m in range(0, 10+1):  #出门买到口罩的次数
        print(m, get_mask(m))  #看剩余只数