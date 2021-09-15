TC = int(input())

for tc in range(1, TC+1):

    text = input()

    result = []
    for te in text:
        if len(result) > 0 and te == result[-1]:
            result.pop(-1)
        else:
            result.append(te)
    print('#{} {}'.format(tc, len(result)))