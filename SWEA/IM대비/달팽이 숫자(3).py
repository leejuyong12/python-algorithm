import sys
sys.stdin = open('달팽이 숫자.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [[0]* N for _ in range(N)]
    K = N
    row = 0
    col = -1
    num = 1
    dir = 1
    while True:
        for j in range(K):
            col += dir
            arr[row][col] = num
            num += 1
        if K == 0:
            break
        K -= 1

        for i in range(K):
            row += dir
            arr[row][col] = num
            num += 1
        dir *= -1
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()