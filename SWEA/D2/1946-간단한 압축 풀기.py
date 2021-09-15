TC = int(input())

for tc in range(1, TC + 1):
    T = int(input())
    base = ''  # base 를 바깥으로 빼내기

    for t in range(1, T + 1):
        Ci, Ki = map(str, input().split())

        base += Ci * int(Ki)
    print('#{}'.format(tc))
    for x in range(0, len(base), 10):
        print(base[x:x + 10])