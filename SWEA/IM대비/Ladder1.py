import sys
sys.stdin = open('Ladder1.txt')

def check(col):
    curR = 99
    curC = col

    while curR > 0:
        curR -= 1
        if curC < 99 and arr[curR][curC+1] == 1:
            while curC < 99 and arr[curR][curC+1] == 1:
                curC += 1

        elif 0 < curC and arr[curR][curC-1] == 1:
            while 0 < curC and arr[curR][curC-1] == 1:
                curC -= 1
    return curC
TC = 10
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for i in range(100):
        if arr[99][i] == 2:
            result = i
    ans = check(result)
    print('#{} {}'.format(tc, ans))

