TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    lst = []

    for x in range(1, N + 1):
        lst.append([0] * x)
    lst[0][0] = 1

    for i in range(1, N):
        for j in range(len(lst[i])):
            if j == 0 or j == i:
                lst[i][j] = 1
            else:
                lst[i][j] = lst[i - 1][j] + lst[i - 1][j - 1]

    print('#{}'.format(tc))
    for a in lst:
        print(*a)