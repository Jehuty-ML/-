
def Comb(m,n):
    if n <= 1 or m==n:
        return 1
    else:
        return Comb(m-1, n) + Comb(m-1, n-1)




if __name__ == '__main__':
    for m in range(1, 11):
        for n in range(m):
            print('C(%s, %s) = %s' % (m, n, Comb(m,n)))