import sys
sys.stdin = open('[반복문1] 숫자사각형2.txt')

TC = int(input())

for tc in range(1, TC+1):
    H, W = map(int, input().split())

    base = [[0]* W for _ in range(H)]
    num = 1
    for y in range(W):
        for x in range(H):
            if y % 2 == 0:
                base[x][y] = num
                num += 1
            elif y % 2 == 1:
                base[x][y] = num
                num += 1
    print('#{}'.format(tc))
    for x in range(H):
        for y in range(W):
            print(base[x][y], end= ' ')
        print()