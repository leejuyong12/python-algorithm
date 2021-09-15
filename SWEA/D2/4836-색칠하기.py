def check(r1, c1, r2, c2, color):
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            if arr[r][c] == 0:
                arr[r][c] = color
            else:
                arr[r][c] = 3


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    arr = [[0]*10 for _ in range(10)]
    for x in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        check(r1, c1, r2, c2, color)

    cnt = 0
    for r in range(len(arr)):
        for c in range(len(arr)):
            if arr[r][c] == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))

