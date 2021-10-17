import sys
sys.stdin = open('중력.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))

    max_cnt = 0
    for x in range(N-1):        # N으로 해도 된다.
        tmp_cnt = 0
        for y in range(x+1, N):
            if lst[x] > lst[y]:
                tmp_cnt += 1
        if tmp_cnt > max_cnt:
            max_cnt = tmp_cnt
            tmp_cnt = 0
    print('#{} {}'.format(tc, max_cnt))