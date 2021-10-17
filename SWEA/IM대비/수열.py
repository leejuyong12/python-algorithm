import sys
sys.stdin = open('수열.txt')

TC = 2
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    max_num = 0
    for x in range(N-K+1):
        tmp_num = 0
        for y in range(K):
            tmp_num += lst[x+y]
        if tmp_num > max_num:
            max_num = tmp_num
    print(max_num)