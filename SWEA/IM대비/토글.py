import sys
sys.stdin = open('토글.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    k = 1
    cnt = 0

    for i in range(N):
        for j in range(N):
            if M % k == 0:
                if arr[i][j] == 1:
                    arr[i][j] = 0
                else:
                    arr[i][j] = 1

            else:
                if (i + j) % k == 0:

                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = 1
            if k == M:
                for x in range(N):
                    for y in range(N):
                        if arr[x][y] == 1:
                            cnt += 1
            k += 1

    print(cnt)
