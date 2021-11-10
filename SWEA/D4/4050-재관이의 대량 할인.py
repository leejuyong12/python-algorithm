import sys
sys.stdin = open('재관이.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    sum_lst = sum(lst)
    for x in range(2, N, 3):
        sum_lst -= lst[x]
    print('#{} {}'.format(tc, sum_lst))

