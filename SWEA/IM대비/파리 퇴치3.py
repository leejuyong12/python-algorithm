import sys
sys.stdin = open('파리 퇴치3.txt')

def method_1(x, y):

    sum1 = sum2 = arr[x][y]       # 처음 뿌린 곳부터 시작작
    for a in range(1, M):         # 0부터 안하는 이유는 나 자신을 계속해서 안더해주기 위해
        if 0 <= x-a:
            sum1 += arr[x-a][y]
        if x+a < N:
            sum1 += arr[x+a][y]
        if 0 <= y-a:
            sum1 += arr[x][y-a]
        if y+a < N:
            sum1 += arr[x][y+a]

    for b in range(1, M):
        if 0 <= x-b and 0 <= y-b:
            sum2 += arr[x-b][y-b]       # 좌상
        if 0 <= x-b and y+b < N:
            sum2 += arr[x-b][y+b]       # 좌하
        if x+b < N and 0 <= y-b:
            sum2 += arr[x+b][y-b]
        if x+b < N and y+b < N:
            sum2 += arr[x+b][y+b]

    return sum1, sum2

# 8방향
dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

def method_2(x, y):
    sum1 = sum2 = arr[x][y]
    for i in range(1, M):
        for j in range(4):
            # 가로세로
            nr = x + dr[j] * i
            nc = y + dc[j] * i

            # 대각선
            nr2 = x + dr[j+4] * i
            nc2 = y + dc[j+4] * i

            # 리스트 범위 이내에만
            if 0 <= nr < N and 0 <= nc < N:
                sum1 += arr[nr][nc]

            if 0 <= nr2 < N and 0 <= nc2 < N:
                sum2 += arr[nr2][nc2]
    return sum1, sum2

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(N):
            sum_fly = max(method_2(i, j))

            if maxV < sum_fly:
                maxV = sum_fly
    print('#{} {}'.format(tc, maxV))



