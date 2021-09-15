def dfs(curX, curY):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    ST = []

    ST.append((curX, curY))
    arr[curY][curX] = 1

    while ST:
        curX, curY = ST.pop()
        # if arr[curY][curX] == 3:
        #     return 1
        for d in range(4):
            newX = curX + dx[d]
            newY = curY + dy[d]

            # if 0 <= newY < N and 0 <= newX < N and arr[newY][newX] == 0:
            #
            if 0 <= newY < N and 0 <= newX < N and arr[newY][newX] != 1:
                if arr[newY][newX] == 3:
                    return 1
                ST.append((newX, newY))
                arr[newY][newX] = 1

    return 0
TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                curX = j
                curY = i
                break

    result = dfs(curX, curY)
    print('#{} {}'.format(tc, result))