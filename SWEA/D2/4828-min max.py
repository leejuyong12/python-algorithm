T = int(input())

for tc in range(T):
    a = int(input())
    N = map(int, input().split())
    lst_N = list(N)

    max_num = lst_N[0]
    min_num = lst_N[0]

    for n in lst_N:
        if n > max_num:
            max_num = n

        elif n < min_num:
            min_num = n

    result = max_num - min_num
    print('#{} {}'.format(tc+1, result))