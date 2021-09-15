def getpage(P,who):
    start = 1
    end = P
    cnt = 0
    while start <= end:
        m = (start+end)//2
        cnt += 1
        if who == m:
            return cnt
        if who < m:
            end = m
        else:
            start = m
    return


TC = int(input())

for tc in range(1, TC+1):
    P, A, B = map(int, input().split())

    who_A = getpage(P, A)
    who_B = getpage(P, B)

    who_win = ''
    if who_A > who_B:
        who_win = 'B'
    elif who_A < who_B:
        who_win = 'A'
    else:
        who_win = '0'

    print('#{} {}'.format(tc, who_win))