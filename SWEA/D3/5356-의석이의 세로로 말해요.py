TC = int(input())

for tc in range(1, TC + 1):
    arr = [0] * 5  # 5줄(row = 5개)
    for z in range(5):
        arr[z] = list(input())

    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    text = ''
    for x in range(max_len):
        for y in range(len(arr)):
            if len(arr[y]) > x:
                text += arr[y][x]

    print('#{} {}'.format(tc, text))