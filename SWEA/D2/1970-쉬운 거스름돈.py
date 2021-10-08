TC = int(input())

won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, TC+1):
    cnt = []
    exc = int(input())
    for x in won:
        a = exc // x
        exc = exc % x
        cnt.append(a)

    print(f'#{tc}')
    print(*cnt)

    # 2
    # 32850
    # 160