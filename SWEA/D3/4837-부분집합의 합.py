TC = int(input())

for tc in range(1, TC+1):
    N, K = map(int, input().split())
    lst = list(range(1,13))

    BITS = 12 # 0b000000000000 ~0b111111111111

    # 101101111111

    cnt_sum = 0
    for i in range(1, 1<<BITS):
        sumV = 0
        cnt = 0

        for j in range(BITS):
            if i & (1<<j): # j번째 비트가 0인지 1인지 확인     # 1&1 일때만 1이다.
                sumV += lst[j]
                cnt += 1
        if sumV == K and cnt == N:
            cnt_sum += 1
    print('#{} {}'.format(tc, cnt_sum))