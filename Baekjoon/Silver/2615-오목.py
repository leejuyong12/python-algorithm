import sys
sys.stdin = open('오목.txt')

N = 19
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # 왜 우상, 우, 우하, 하 만 고려하는거지???

def omok():
    for x in range(N):
        for y in range(N):
            if arr[x][y]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1

                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue

                    while 0 <= nx < N and 0 <= ny < N and arr[x][y] == arr[nx][ny]:
                        cnt += 1
                        if cnt == 5: # 5개를 셌는데
                            if 0 <= nx + dx[i] < N and 0 <= ny + dy[i] < N and arr[nx][ny] == arr[nx + dx[i]][ny + dy[i]]:
                                break
                            if 0 <= x - dx[i] < N and 0 <= y - dy[i] < N and arr[x][y] == arr[x - dx[i]][y - dy[i]]:
                                break
                            return arr[x][y], x+1, y+1
                        nx += dx[i]
                        ny += dy[i]
    return 0, -1, -1
color, x, y = omok()
if not color:
    print(color)
else:
    print(color)
    print(x, y)