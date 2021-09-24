import sys
sys.stdin = open('탈주범 검거.txt')
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],   # 상하좌우
    [0, 1, 0, 1],   # 상하
    [1, 0, 1, 0],   # 좌우
    [1, 0, 0, 1],   # 상우
    [1, 1, 0, 0],   # 하우
    [0, 1, 1, 0],   # 하좌
    [0, 0, 1, 1]   # 상좌
]

TC = int(input())

for tc in range(1, TC+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]   # 시간 겸 방문체크용

    Q = [(R, C)]
    visited[R][C] = 1
    ans = 0
    while Q:
        r, c = Q.pop(0)
        ans += 1

        if visited[r][c] >= L: continue

        # 사방향 탐색
        for d in range(4):
            curr_p = tunnel[r][c]
            if pipe[curr_p][d] == 0: continue

            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue # 좌표 벗어났을때

            nd = (d+2) % 4  # 다음 방향
            np = tunnel[nr][nc]           # 다음 파이프

            if visited[nr][nc] or pipe[np][nd] == 0: continue  # 방문했거나 다음 좌표의 파이프가 현재 좌표와 연결되지 않는다면


            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))
    print('#{} {}'.format(tc, ans))