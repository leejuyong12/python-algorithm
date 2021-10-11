import sys
sys.stdin = open('[반복문3] 문자삼각형2.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    # base = [[0]* N for _ in range(N)]
    # text = 65
    # for x in range(N//2+1):
    #     for y in range(N//2-x, N//2+x+1):
    #         base[y][N//2-x] = chr(text)
    #         text += 1
    #         if text > 90:
    #             text = 65
    # print('#{}'.format(tc))
    # for i in range(N):
    #     for j in range(N//2):
    #         if base[i][j] == 0:
    #             print('')
    #         else:
    #             print('{%c}'.format(base[i][j]))
    #     print('\n')

    lst = []
    text = 65
    for x in range(1, N+1):
        lst.append([0] * x)
    lst[0][0] = chr(text)
    text += 1
    for i in range(N//2, -1, -1):
        for j in range(i, N-i):
            lst[j][i] = chr(text)
            text += 1
            if text > 90:
                text = 65
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 0:
                print(' ')
            else:
                print(lst[i][j], end = ' ')
        print('\n')
    # for i in range(1, N):
    #     for j in range(len(lst[i])):
    #         if j == 0:
    #             lst[i][j] = chr(text)
    #             text += 1
    #         else:
    #             lst[i][j] = chr(text)
    #             text += 1
    print('#{}'.format(tc))
    for a in lst:
        print(*a)
