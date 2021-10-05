import sys
sys.stdin = open('화물도크.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    truck = [list(map(int, input().split())) for _ in range(N)]

    # 정렬하기
    for i in range(N):
        for j in range(i, N):
            if truck[i][1] > truck[j][1]:
                truck[i], truck[j] = truck[j], truck[i]

    visited = [0] * N
    visited[0] = 1
    result = [truck[0]]

    for x in range(N):
        if result[-1][1] > truck[x][0]:
            visited[x] = 1
    # 다 1로 바뀌었으면 break
    if 0 not in visited:
        break