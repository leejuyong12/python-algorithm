# 최대공약수 구하는 함수
def div(n, m):
    while n % m != 0:
        mod = n % m
        n = m
        m = mod
    return m


n, m = map(int, input().split(':'))
x = div(n, m)
print('{}:{}'.format(n//x, m//x))

