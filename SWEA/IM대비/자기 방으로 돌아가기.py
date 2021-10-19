TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    bok = [0] * 201
    for n in range(N):
        start, end = map(int, input().split())

        if start > end:
            start, end = end, start
        start = (start+1) // 2
        end = (end+1) // 2
        for j in range(start, end+1):
            bok[j] += 1
    print('#{} {}'.format(tc, max(bok)))