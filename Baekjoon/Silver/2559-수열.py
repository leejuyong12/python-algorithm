import sys
sys.stdin = open('2559-백준-수열.txt')
import time
start = time.time()

TC = 2
for tc in range(1, TC+1):
    N, K = map(int, input().split())    # N개의 정수, K개의 합
    arr = list(map(int, input().split()))

    base_num = 0
    for k in range(K):
        base_num += arr[k]

    max_num = base_num
    for n in range(1, N-K+1):
        base_num = base_num - arr[n-1] + arr[n+K-1]

        if max_num < base_num:
            max_num = base_num
    print(max_num)
    # max_sum = 0
    # for x in range(N-K+1):
    #     sum_num = 0
    #     for y in range(K):
    #         sum_num += arr[x+y]
    #     if max_sum < sum_num:
    #         max_sum = sum_num
    # print(max_sum)

    # sum_lst = []
    # for x in range(N-K+1):
    #     sum_num = 0
    #     for y in range(K):
    #         sum_num += arr[x + y]
    #     sum_lst.append(sum_num)
    # max_num = sum_lst[0]
    # for m in range(1, len(sum_lst)):
    #     if sum_lst[m] > max_num:
    #         max_num = sum_lst[m]
    # print(max_num)
print(time.time()-start)

