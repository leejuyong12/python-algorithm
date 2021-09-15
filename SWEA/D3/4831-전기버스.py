TC = int(input())
for tc in range(1, TC+1):
    K, N, M = map(int, input().split())
    CHARGE = list(map(int, input().split()))

# 방법1 - 정류장으로 생각
    curp = 0
    cnt = 0
    while curp < N:
        nextp = curp + K
        if nextp >= N:
            break
        if nextp in CHARGE:
            cnt += 1
            curp = nextp
        else:
            while curp < nextp and nextp not in CHARGE:
                nextp -= 1

            if curp == nextp:
                cnt = 0
                break
            if nextp in CHARGE:  # else: 로 써도 됨
                cnt += 1
                curp = nextp

            # nextp의 값을 하나씩 빼면서(앞으로 가면서) 충전기가 있는지 확인
    print('#{} {}'.format(tc, cnt))