import sys
sys.stdin = open('디저트 카페.txt')

def clearvisited():
    for i in range(101):
        visited[i] = False

# 반복문을 사용
def solve():
    global maxV
    for i in range(N-1):
        for j in range(N-1):
            for a in range(1, N-1):
                for b in range(1, N-1):
                    # i, j에서 시작하여 a, b의 크기를 갖는 사각형을 가정한다.
                    clearvisited()
                    curX = j
                    curY = i
                    isError = False
                    # 우상으로 a 만큼 이동하면서 가능한지 확인한다.
                    for k in range(a):
                        curX += 1
                        curY -= 1
                        if curX >= N or curY < 0 or visited[arr[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[arr[curY][curX]] = True
                    if isError:
                        continue
                    # 우하로 b만큼 이동하면서 가능한지 확인한다.
                    for k in range(b):
                        curX += 1
                        curY += 1
                        if curX >= N or curY >= N or visited[arr[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[arr[curY][curX]] = True
                    if isError:
                        continue
                    # 좌하
                    for k in range(a):
                        curX -= 1
                        curY += 1
                        if curX < 0 or curY >= N or visited[arr[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[arr[curY][curX]] = True
                    if isError:
                        continue
                    # 좌상
                    for k in range(b):
                        curX -= 1
                        curY -= 1
                        if curX < 0 or curY < 0 or visited[arr[curY][curX]]:
                            isError = True
                            break
                        else:
                            visited[arr[curY][curX]] = True
                    if isError:
                        continue
                    # 최대 길이를 계산한다.
                    if (a+b)*2 > maxV:
                        maxV = (a+b)*2

# 재귀를 이용하는 방법
DI = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
def solve2(curY, curX, curD, k):
    # if k == N:        # 이 방법 안된다
    #     return
    global maxV
    # 이미 지나온 길이면
    for i in range(1, k-1):
        if res[i][2] == arr[curY][curX]:
            return
    # 좌상의 방향이면서 원 경로로 돌아왔으면
    if curD == 3 and curX == res[0][0] and curY == res[0][1]:
        if k > maxV:
            maxV = k
        return
    # 방향 유지
    dy, dx = DI[curD]
    if 0 <= curY+dy < N and 0 <= curX+dx < N:
        res[k] = (curX, curY, arr[curY][curX])
        solve2(curY+dy, curX+dx, curD, k+1)

    # 방향전환 한 경우
    if curD < 3:
        dy, dx = DI[curD + 1]
        if 0 <= curY + dy < N and 0 <= curX + dx < N:
            res[k] = (curX, curY, arr[curY][curX])
            solve2(curY+dx, curX+dy, curD+1, k+1)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # res = [(-1, -1, -1)] * (N*N)
    # maxV = 0
    # for i in range(N):
    #     for j in range(N):
    #         res[0] = (j, i, arr[i][j])
    visited = [False] * 101
    maxV = -1
    solve()
    print('#{} {}'.format(tc, maxV))