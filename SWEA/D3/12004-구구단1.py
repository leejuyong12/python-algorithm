TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    multiple = []

    for x in range(1, 10):
        for y in range(1, 10):
            multiple.append(x * y)
    result = ''
    if N in multiple:
        result = 'Yes'
    else:
        result = 'No'
    print('#{} {}'.format(tc, result))