import sys
sys.stdin = open('달팽이 숫자.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [[0]* N for _ in range(N)]

    K = N
    dir = 1
    row = 0
    col = -1
    num = 1

    while True:
        # 수평이동
        for x in range(K):
            col += dir
            arr[row][col] = num
            num += 1
        K -= 1
        if K == 0:
            break
        # 수직이동
        for y in range(K):
            row += dir
            arr[row][col] = num
            num += 1
        dir *= -1
    print('#{}'.format(tc))
    for x in range(N):
        for y in range(N):
            print(arr[x][y], end=' ')
        print()