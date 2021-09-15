def maxP(lst):
    max_num = lst[0]
    maxp = 0

    for x in range(1, len(lst)):
        if lst[x] > max_num:
            max_num = lst[x]
            maxp = x
    return maxp


def minP(lst):
    min_num = lst[0]
    minp = 0

    for x in range(1, len(lst)):
        if lst[x] < min_num:
            min_num = lst[x]
            minp = x
    return minp


TC = 10
for tc in range(1, TC + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N):
        lst[maxP(lst)] -= 1
        lst[minP(lst)] += 1
    final_maxp = lst[maxP(lst)]
    final_minp = lst[minP(lst)]
    print('#{} {}'.format(tc, final_maxp - final_minp))