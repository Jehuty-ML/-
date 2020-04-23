'''
数学归纳法：1归纳边界 2.归纳假设N=k， 3.归纳推导 n=k+1
递归： 1递归边界n=0 or n=1 2.递归假设 3.归纳推导
数学是证明，递归不是，但同样可以三步走  0.递归参数--盘子  1.递归边界-- 盘子为1时  2.递归假设--直接移动N-1个盘
'''



def hanoi(panes, src, buffer, dest):
    if panes == 1:
        print('move no.1 from %s to %s' % (src, dest))
    else:
        hanoi(panes-1, src, dest, buffer)
        print('put no.%s from %s to %s' % (panes, src, dest))
        hanoi(panes-1, buffer, src, dest)



if __name__ == '__main__':
    hanoi(3, 'a', 'b', 'c')