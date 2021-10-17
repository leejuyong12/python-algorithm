import sys
sys.stdin = open('진기의 최고급 붕어빵.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M, K = map(int, input().split())
    comein = list(map(int, input().split()))
    max_time = max(comein)
    counting_customer = [0] * (max_time+1)

    comein.sort()
    for x in comein:
        counting_customer[x] += 1
    bread = 0
    for y in range(len(counting_customer)):
        if y > 0 and y % M == 0:
            bread += K
        bread -= counting_customer[y]

        if bread < 0:
            break
    if bread < 0:
        print('#{} {}'.format(tc, 'Impossible'))
    else:
        print('#{} {}'.format(tc, 'Possible'))






