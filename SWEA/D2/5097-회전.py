TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    ST = []
    for x in range(M):
        ST.append(lst.pop(0))
        lst.append(ST.pop(0))

    print('#{} {}'.format(tc, lst[0]))