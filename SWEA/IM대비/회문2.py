import sys
sys.stdin = open('회문2.txt')

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
    # 가로 검사
    for x in range(100):
        for y in range(100-M+1):
            res_row = check(arr[x][y:y+M])
            if res_row:
                return arr[x][y:y+M]

    # 세로 검사
    for x in range(100):
        for y in range(100-M+1):
            temp_col = ''
            for z in range(y, y+M):
                temp_col += arr[z][x]
            res_col = check(temp_col)
            if res_col:
                return temp_col
TC = 10
for tc in range(1, TC+1):
    t = int(input())
    arr = [list(input()) for _ in range(100)]

    for x in range(100, 1, -1):
        final_res = CC(x)
        if final_res:
            break
    print('#{} {}'.format(t, len(final_res)))