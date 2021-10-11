import sys
sys.stdin = open('구간합.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())

    lst = list(map(int, input().split()))

    max_sum = 0
    min_sum = 987654321
    for x in range(N-M+1):
        tmp_sum = 0
        for y in range(x, x+M):
            tmp_sum += lst[y]
        if tmp_sum > max_sum:
            max_sum = tmp_sum
        if tmp_sum < min_sum:
            min_sum = tmp_sum
    print('#{} {}'.format(tc, max_sum-min_sum))