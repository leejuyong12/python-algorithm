import sys
sys.stdin = open('최소합.txt')

def check(x, y, total):
    global result, dy, dx, visited
    if x == N-1 and y == N-1:
        total += arr[x][y]

        if total < result:
            result = total
            return result

    if total > result:      # 이거 안넣으면 시간초과
        return              # 이미 result보다 크면 필요없음

    for i in range(2):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if x > N-1 or y > N-1:
            continue
        if not visited[y][x]:
            visited[y][x] = 1
            check(new_x, new_y, total + arr[y][x])
            visited[y][x] = 0


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dy = [0, 1]
    dx = [1, 0]

    visited = [[0] * N for _ in range(N)]
    result = (N*2-1) * 10  # 3 - 5  4 - 7  5 - 9
    check(0, 0, 0)
    print('#{} {}'.format(tc, result))

