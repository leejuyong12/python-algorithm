def bfs(curX, curY):

    Q = []
    visited = [[-1] * N for _ in range(N)]
    # 시작점 큐에 넣는다.
    Q.append((curX, curY))
    visited[curY][curX] = 0
    while Q:
        curX, curY = Q.pop(0)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            newX = curX + dx
            newY = curY + dy
            if 0 <= newX < N and 0 <= newY < N and visited[newY][newX] == -1:
                if arr[newY][newX] == '3':  # 문자열로 입력 받았다.
                    return visited[curY][curX]
                if arr[newY][newX] == '0':   # 문자열로 입력받았다.
                    Q.append((newX, newY))
                    visited[newY][newX] = visited[curY][curX] + 1
    return 0
        #인접한 w중 방문안한 것을 찾아서 큐에 넣고 방문표시한다.

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [input() for _ in range(N)] # 체크

    for i in range(N):
        if '2' in arr[i]:   # arr[i].count('2') > 0:
            curX = arr[i].index('2')
            curY = i
            break

    print('#{} {}'.format(tc, bfs(curX, curY)))