TC = int(input())

for tc in range(1, TC+1):
    A, B = map(int, input().split())
    pal = []
    cnt = 0
    for x in range(A, B+1):
        if str(x) == str(x)[::-1]:
            pal.append(x)
    for y in pal:
        for z in range(32):
            if y == z**2:
                num = z
                if str(num) == str(num)[::-1]:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))