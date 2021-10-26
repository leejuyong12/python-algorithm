# 1은 그대로 2는 좌우반전 3은 상하 반전
import sys
sys.stdin = open('마법 거울.txt')
N = int(input())
arr = [list(input()) for _ in range(N)]
K = int(input())
new_arr = [['']*N for _ in range(N)]
if K == 1:
    for x in range(N):
        for y in range(N):
            new_arr[x][y] = arr[x][y]
elif K == 2:
    for x in range(N):
        for y in range(N):
            new_arr[x][y] = arr[x][N-y-1]
elif K == 3:
    for x in range(N):
        for y in range(N):
            new_arr[x][y] = arr[N-x-1][y]
for x in range(N):
    for y in range(N):
        print(new_arr[x][y], end='')
    print()
