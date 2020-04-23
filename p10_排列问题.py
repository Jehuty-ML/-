


def A(m,n):
    if n <= 1:
        return 1
    else:
        result = n * A(m-1, n-1)
        if m>n:
            result += A(m-1, n)
        return result

if __name__ == '__main__':
    for m in range(1, 11):
        for n in range(m):
            print('A(%s, %s) = %s' % (m, n, A(m,n)))





