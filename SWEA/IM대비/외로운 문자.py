import sys
sys.stdin = open('외로운 문자.txt')

TC = int(input())
for tc in range(1, TC+1):
    text = list(input())
    tmp = []
    for x in range(len(text)):
        if text[x] not in tmp:
            tmp.append(text[x])
        else:
            tmp.pop(tmp.index(text[x]))
    tmp.sort()
    res = ''
    if tmp:
        for y in range(len(tmp)):
            res += tmp[y]
    else:
        res += 'Good'

    print('#{} {}'.format(tc, res))