import sys
sys.stdin = open('View.txt')

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))
    res = 0
    for x in range(2, N-2):
        if lst[x] - lst[x-2] >= 1 and lst[x] - lst[x-1] >= 1 and lst[x] - lst[x+1] >= 1 and lst[x] - lst[x+2] >= 1:
           res += lst[x] - max(lst[x-2], lst[x-1], lst[x+1], lst[x+2])
    print('#{} {}'.format(tc, res))