import sys
sys.stdin = open('진기의 최고급 붕어빵.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M, K = map(int, input().split())         # N명의 손님, M초의 시간으로 붕어빵 K개 만들수 있다.
    nums = list(map(int, input().split()))      # N개의 정수, 손님이 도착하는 초

    # 기다리는 시간 없이 줄 수 있으면 Possible 기다리는 시간이 발생하면 Impossible
    customer = [0] * 11112     # 손님이 오는 시간=index 값
    for x in nums:
        customer[x] += 1

    bungeoppang = 0
    for y in range(11112):
        if y > 0 and y % M == 0:
            bungeoppang += K
        bungeoppang -= customer[y]

        if bungeoppang < 0:
            break
    if bungeoppang < 0:
        print('#{} {}'.format(tc, 'Impossible'))
    else:
        print('#{} {}'.format(tc, 'Possible'))





