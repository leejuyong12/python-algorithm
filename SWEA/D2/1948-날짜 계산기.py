import sys
sys.stdin = open('1948-날짜계산기.txt')

TC = int(input())

for tc in range(1, TC + 1):
    m1, d1, m2, d2 = map(int, input().split())

    # 1/31, 2/28, 3/31, 4/30, 5/31, 6/30,
    # 7/31, 8/31, 9/30, 10/31, 11/30, 12/31

    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    day = d2

    if m2 >= m1 + 1:
        for x in range(m1 + 1, m2):
            day += days[x]
        day += days[m1] - d1 + 1

    print('#{} {}'.format(tc, day))
