def check(x, sum_num):
    global result
    if result <= sum_num:
        return

    if x == N:
        if sum_num >= B:
            result = sum_num
        return

    if visited[x] == 0:
        visited[x] = 1
        check(x+1, sum_num + lst[x])
    if visited[x] == 1:
        visited[x] = 0
        check(x+1, sum_num)


TC = int(input())

for tc in range(1, TC+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 987654321
    visited = [0] * N

    check(0, 0)
    print('#{} {}'.format(tc, result-B))


