TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    income = list(map(int, input().split()))

    sum_income = sum(income)

    avg_income = sum_income / N
    cnt = 0
    for x in income:
        if x <= avg_income:
           cnt += 1
    print('#{} {}'.format(tc, cnt))