TC = int(input())

for tc in range(1, TC+1):
    text = list(input())

    base = []
    for x in range(len(text)):
        if text[x] in base:
            base.pop(base.index(text[x]))       # base에 있다면 그걸 빼준다
        elif text[x] not in base:
            base.append(text[x])                # base에 없다면 반복문을 통해 나온 걸 더해준다
    result = ''
    if not base:
        print('#{} {}'.format(tc, 'Good'))
    else:
        base = sorted(base)                     # 사전 순서대로
        for y in base:
            result += y
        print('#{} {}'.format(tc, result))