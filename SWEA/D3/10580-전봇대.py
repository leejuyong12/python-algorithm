import sys
sys.stdin = open('전봇대.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for x in range(N):
        for y in range(x+1, N):
            if arr[x][0] < arr[y][0] and arr[x][1] > arr[y][1]:
                cnt += 1
    print('#{} {}'.format(tc, cnt))
