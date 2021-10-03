TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    start = 1
    result = 0
    base = set()
    while True:
        for i in str(start * N):
            if not i in base:
                base.add(i)     # set에는 add활용
        if len(base) == 10:
            result = start * N
            break
        start += 1
    print('#{} {}'.format(tc, result))