def check(str0):  # 회문인지 체크

    st = 0
    ed = len(str0) - 1
    while st < ed and str0[st] == str0[ed]:
        st += 1
        ed -= 1
    if st >= ed:
        return True
    return False


def CC(M):
    # 회문을 찾아서 return
    # 가로
    for row in range(N):
        for st in range(N - M + 1):
            result_r = check(arr[row][st:st + M])
            if result_r:
                return arr[row][st:st + M]

    # 세로
    for column in range(N):
        for st in range(N - M + 1):
            temp_str = ''
            for k in range(st, st + M):
                temp_str += arr[k][column]
            result_c = check(temp_str)
            if result_c:
                return temp_str


TC = 10
for tc in range(1, TC + 1):
    N = 100
    T = int(input())
    arr = [input() for _ in range(N)]

    for M in range(N, 2, -1):
        result = CC(M)

        if result:
            break
    print('#{} {}'.format(tc, len(result)))