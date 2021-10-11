import sys
sys.stdin = open('[반복문1] 숫자사각형1.txt')

TC = int(input())

for tc in range(1, TC+1):
    H, W = map(int, input().split())

    base = [[0]*W for _ in range(H)]
    num = 1
    for x in range(H):
        for y in range(W):
            base[x][y] = num
            num += 1
    print('#{}'.format(tc))
    for i in range(H):
        for j in range(W):
            print(base[i][j], end = ' ')
        print()