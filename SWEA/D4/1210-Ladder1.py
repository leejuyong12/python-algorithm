def isFind(col):
    curR = 99
    curC = col

    while curR > 0:
        curR -= 1
        if curC < 99 and line[curR][curC + 1] == 1:  # 오른쪽으로 가는 경우
            while curC < 99 and line[curR][curC + 1] == 1:
                curC += 1

        elif curC > 0 and line[curR][curC - 1] == 1:  # 왼쪽으로 가는 경우
            while curC > 0 and line[curR][curC - 1] == 1:
                curC -= 1

    return curC


TC = 10

for tc in range(1, TC + 1):
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for i in range(100):
        # 도착지점이 2인 지점부터 올라감
        if line[99][i] == 2:
            result = i
    ans = isFind(result)
    print('#{} {}'.format(tc, ans))