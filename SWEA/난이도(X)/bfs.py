def bfs(curX, curY):
    Q = []
    visited = [[-1] * 16 for _ in range(16)]
    Q.append((curX, curY))
    visited[curY][curX] = 0
    while Q:
        curX, curY = Q.pop(0)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newX = curX + dx
            newY = curY + dy
            if 0 <= newX < 16 and 0 <= newY < 16 and visited[newY][newX] == -1:
                if arr[newY][newX] == '3':
                    return 1
                if arr[newY][newX] == '0':
                    Q.append((newX, newY))
                    visited[newY][newX] = visited[curY][curX] + 1
    return 0


TC = 10
for tc in range(1, TC + 1):
    t = int(input())
    arr = [input() for _ in range(16)]

    for i in range(16):
        if '2' in arr[i]:
            curX = arr[i].index('2')
            curY = i
            break

    print('#{} {}'.format(t, bfs(curX, curY)))