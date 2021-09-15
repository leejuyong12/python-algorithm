TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    base = [int(input()) for _ in range(N)]

    avg = sum(base) // len(base)
    cnt = 0
    while True:
        if max(base) == avg:
            break
        else:
            for x in range(len(base)):
                if base[x] > avg:
                    cnt += base[x] - avg
                    base[x] = avg
                    break
    print('#{} {}'.format(tc, cnt))