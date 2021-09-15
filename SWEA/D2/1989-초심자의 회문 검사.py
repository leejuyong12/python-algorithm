pd = int(input())

for a in range(pd):
    cnt = 0
    x = input()

    if x == x[::-1]:
        cnt += 1
    print(f'#{a + 1} {cnt}')