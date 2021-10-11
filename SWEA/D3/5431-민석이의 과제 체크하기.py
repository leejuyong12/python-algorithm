TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    done = list(map(int, input().split()))

    not_done = []
    for x in range(1, N+1):
        if x not in done:
            not_done.append(x)
    not_done.sort()
    result = ''
    for y in not_done:
        result += str(y) + ' '
    print('#{} {}'.format(tc, result))

