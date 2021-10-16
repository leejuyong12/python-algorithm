import sys
sys.stdin = open('부분집합의 합.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())

    # 1 <= A <= 12   ,      N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수

    lst = list(range(1, 13))

    BITS = 12

    cnt_sum = 0
    for i in range(1, 1<<BITS):
        sumV = 0
        cnt = 0
        for j in range(BITS):
            if i & (1<<j):
                sumV += lst[j]
                cnt += 1
        if sumV == K and cnt == N:
            cnt_sum += 1
    print('#{} {}'.format(tc, cnt_sum))
