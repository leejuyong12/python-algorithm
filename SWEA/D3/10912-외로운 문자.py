TC = int(input())

for tc in range(1, TC+1):
    text = list(input())

    base = []
    for x in range(len(text)):
        if text[x] in base:
            base.pop(base.index(text[x]))       # 똑같은 문자가 있는 (base의 index를 활용해서) base에 있다면 그걸 빼준다
        elif text[x] not in base:
            base.append(text[x])                # base에 없다면 base에 append해준다

    result = ''
    if not base:                                # base가 다 비어있다면 Good 출력
        print('#{} {}'.format(tc, 'Good'))

    else:
        base = sorted(base)                     # base에 남은게 있다면 사전 순서대로
        for y in base:
            result += y

        print('#{} {}'.format(tc, result))