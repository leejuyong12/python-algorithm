TC = int(input())
for tc in range(1, TC + 1):
    nums = int(input())

    a, b, c, d, e = 0, 0, 0, 0, 0
    while nums > 1:
        if nums % 11 == 0:
            nums = nums // 11
            e += 1
        if nums % 7 == 0:
            nums = nums // 7
            d += 1
        if nums % 5 == 0:
            nums = nums // 5
            c += 1
        if nums % 3 == 0:
            nums = nums // 3
            b += 1
        if nums % 2 == 0:
            nums = nums // 2
            a += 1
    print('#{}'.format(tc), a, b, c, d, e)