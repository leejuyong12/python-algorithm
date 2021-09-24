import sys
sys.stdin = open('등산로 조성.txt')
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def work(r, c, road, skill):    # road는 조성된 등산로의 길이, skill은 공사유무
    global result
    if road > result:
        result = road

    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if arr[r][c] > arr[nr][nc]:     #현재보다 낮은 곳으로 이동할때
                work(nr, nc, road+1, skill)
            elif skill and arr[r][c] > arr[nr][nc] - K:# 현재보다 높거나 같은 위치로 이동할 때
                tmp = arr[nr][nc]
                arr[nr][nc] = arr[r][c] - 1
                work(nr, nc, road+1, 0)
                arr[nr][nc] = tmp
    visited[r][c] = 0

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0

    for x in range(N):
        for y in range(N):
            if max_h < arr[x][y]:
                max_h = arr[x][y]

    visited = [[0] * N for _ in range(N)]
    result = 0

    for x in range(N):
        for y in range(N):
            if arr[x][y] == max_h:
                work(x, y, 1, 1)

    print('#{} {}'.format(tc, result))