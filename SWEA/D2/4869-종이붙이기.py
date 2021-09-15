def recur(N):


    N = N // 10
    r = [1, 3]
    for i in range(2, N+1):
        r.append(r[i-1]+r[i-2]*2)

    return r[N-1]
TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    ans = recur(N)

    print('#{} {}'.format(tc, ans))