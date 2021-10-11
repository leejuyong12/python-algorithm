import sys
sys.stdin = open('[반복문2] 문자사각형2.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    base = [[0] * N for _ in range(N)]
    text = 65
    for y in range(N):
        for x in range(N):
            if y % 2 == 0:
                base[x][y] = chr(text)
                text += 1
                if text > 90:    # ord('Z') = 90
                    text = 65
            elif y % 2 == 1:
                base[N-1-x][y] = chr(text)
                text += 1
                if text > 90:
                    text = 65
    print('#{}'.format(tc))
    for x in range(N):
        for y in range(N):
            print(base[x][y], end=' ')
        print()