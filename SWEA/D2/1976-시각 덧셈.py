TC = int(input())
for tc in range(1, TC + 1):
    h1, m1, h2, m2 = map(int, input().split())

    h3 = h1 + h2
    m3 = m1 + m2

    if m3 >= 60:
        h3 = h3 + 1
        m3 = m3 - 60

    if h3 > 12:
        h3 = h3 - 12

    print('#{} {} {}'.format(tc, h3, m3))