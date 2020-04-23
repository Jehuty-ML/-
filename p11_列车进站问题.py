
def get_train(n,m=0):
    if n == 0:
        return 1
    result = get_train(n-1, m+1)  #一辆车从开始区进入中转区
    if m > 0:  #算多少种可能性，所有有车就一定出去，算可能性
        result += get_train(n-1, m-1)  #一辆车从中转区驶出
    return result


if __name__ == '__main__':
    for n in range(1, 10+1):
        print(n, get_train(n))