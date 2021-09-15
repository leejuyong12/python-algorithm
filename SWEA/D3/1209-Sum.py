TC = 10

for tc in range(1, TC + 1):
    a = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    lst = []

    # 행 순회
    for i in range(len(arr)):
        sum_hor = 0
        for j in range(len(arr[i])):
            sum_hor += arr[i][j]
        lst.append(sum_hor)

    # 열 순회
    for j in range(len(arr)):
        sum_ver = 0
        for i in range(len(arr[0])):
            sum_ver += arr[i][j]
        lst.append(sum_ver)

    # 대각선 순회
    sum_dia = 0
    for i in range(len(arr)):
        sum_dia += arr[i][i]
    lst.append(sum_dia)

    # 반대 대각선 순회
    sum_dia_rev = 0
    for i in range(len(arr)):
        sum_dia_rev += arr[i][99 - i]
    lst.append(sum_dia_rev)

    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num

    print('#{} {}'.format(a, max_num))