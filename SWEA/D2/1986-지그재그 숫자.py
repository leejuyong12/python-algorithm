T = int(input())

for x in range(T):

    num = int(input())
    a = 0
    for y in range(1, num + 1):
        if y % 2 == 1:
            a += y
        elif y % 2 == 0:
            a -= y
    print(f'#{x + 1} {a}')