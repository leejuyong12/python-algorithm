import sys
sys.stdin = open('이진탐색.txt')

def getpage(P, who):
    st = 1
    ed = P
    cnt = 0
    while st < ed:
        m = (st + ed) // 2
        cnt += 1
        if who == m:
            return cnt
        if who < m:
            ed = m
        else:
            st = m
    return
TC = int(input())
for tc in range(1, TC+1):
    P, A, B = map(int, input().split())

    who_A = getpage(P, A)
    who_B = getpage(P, B)

    if who_A > who_B:
        who_win = 'B'
    elif who_A < who_B:
        who_win = 'A'
    else:
        who_win = 0
    print('#{} {}'.format(tc, who_win))