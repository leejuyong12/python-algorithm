import sys
sys.stdin = open('회문.txt')

def check(arr):
    st = 0
    ed = len(arr)-1
    while st < ed and arr[st] == arr[ed]:
        st += 1
        ed -= 1
    if st >= ed:
        return True
    return False

def CC(M):
    for x in range(N):
        for y in range(N-M+1):
            res_row = check(lst[x][y:y+M])
            if res_row:
                return lst[x][y:y+M]

    for x in range(N):
        for y in range(N-M+1):
            tmp_col = ''
            for z in range(y, y+M):
                tmp_col += lst[z][x]
            res_col = check(tmp_col)
            if res_col:
                return tmp_col

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]

    res = ''
    for x in range(M):
        res += CC(M)[x]

    print('#{} {}'.format(tc, res))
