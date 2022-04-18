import sys
sys.stdin = open('경로찾기.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
base = [[0]* N for _ in range(N)]

# 플로이드와샬은 3중 for문 사용하더라..
for x in range(N):  # 경유
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 or (arr[i][x] == 1 and arr[x][j] == 1):
                arr[i][j] = 1
for x in range(N):
    for y in range(N):
        print(arr[x][y], end=' ')
    print()