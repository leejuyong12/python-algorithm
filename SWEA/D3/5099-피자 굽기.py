TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Ci = [0] + list(map(int, input().split()))
    Q = [0] * N

    newpizza = 1

    while Q:
        pizza = Q.pop(0)
        Ci[pizza] = Ci[pizza] // 2
        if Ci[pizza] == 0:
            if newpizza <= M:
                Q.append(newpizza)
                newpizza += 1
        else:
            Q.append(pizza)
    print('#{} {}'.format(tc, pizza))