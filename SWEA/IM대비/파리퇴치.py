import sys
sys.stdin = open('파리퇴치.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp_sum = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    tmp_sum += arr[x][y]
            if tmp_sum > max_sum:
                max_sum = tmp_sum
    print('#{} {}'.format(tc, max_sum))

