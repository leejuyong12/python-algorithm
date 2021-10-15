import sys
sys.stdin = open('진기의 최고급 붕어빵.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M, K = map(int, input().split())     # N명의 손님, M초의 시간으로 K개의 붕어빵 만들 수 있다.
    customer_time = list(map(int, input().split()))
    max_time = max(customer_time)
    counting_customer = [0] * (max_time+1)   # 각 초에 오는 손님 counting
    for x in customer_time:
        counting_customer[x] += 1

    bread = 0                           # M초마다 K만큼의 붕어빵 추가
    for y in range(max_time+1):
        if y > 0 and y % M == 0:
            bread += K
        bread -= counting_customer[y]   # 손님이 오는 초에 붕어빵 하나씩 빼기

        if bread < 0:                   # 붕어빵이 음수가 되면(기다리는 시간 발생) break
            break
    if bread < 0:
        print('#{} {}'.format(tc, 'Impossible'))
    else:
        print('#{} {}'.format(tc, 'Possible'))










