T = int(input())

won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for ex in range(T):
    cnt = []
    exc = int(input())
    for x in won:
        a = exc // x
        exc = exc % x
        cnt.append(a)

    print(f'#{ex + 1}')
    print(*cnt)