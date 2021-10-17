import sys
sys.stdin = open('파스칼의 삼각형.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    arr[0][0] = 1
    for i in range(1, N):
        for j in range(N):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print('#{}'.format(tc))
    for x in range(N):
        for y in range(N):
            if arr[x][y] != 0:
                print(arr[x][y], end=' ')
        print()