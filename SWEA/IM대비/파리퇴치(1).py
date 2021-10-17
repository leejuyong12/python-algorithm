import sys
sys.stdin = open('파리퇴치.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            tmp_num = 0
            for i in range(x, x+M):
                for j in range(y, y+M):
                    tmp_num += arr[i][j]
            if max_num < tmp_num:
                max_num = tmp_num
    print('#{} {}'.format(tc, max_num))
