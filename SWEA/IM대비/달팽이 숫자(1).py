import sys
sys.stdin = open('달팽이 숫자.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    K = N
    num = 1
    row = N
    col = 0
    row_dir = -1
    col_dir = 1
    while True:

        for j in range(K):
            row += row_dir
            arr[row][col] = num
            num += 1
        if K == 0:
            break
        K -= 1
        for i in range(K):
            col += col_dir
            arr[row][col] = num
            num += 1

        row_dir *= -1
        col_dir *= -1
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()