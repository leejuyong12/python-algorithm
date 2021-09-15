TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    sum_lst = []
    for a in range(N-M+1):
        sum_num = 0

        for b in range(M):
            sum_num += A[a+b]
        sum_lst.append(sum_num)

    max_num = sum_lst[0]
    min_num = sum_lst[0]
    for num in range(1, len(sum_lst)):
        if sum_lst[num] > max_num:
            max_num = sum_lst[num]
        if sum_lst[num] < min_num:
            min_num = sum_lst[num]

    print('#{} {}'.format(tc, max_num-min_num))
