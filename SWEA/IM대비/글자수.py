import sys
sys.stdin = open('글자수.txt')

TC = int(input())
for tc in range(1, TC+1):
    base = list(input())
    text = list(input())

    lst = []
    for x in range(len(base)):
        if base[x] not in lst:
            lst.append(base[x])

    dict_base = {}
    for y in lst:
        dict_base[y] = 0

    for z in range(len(text)):
        if text[z] in dict_base.keys():
            dict_base[text[z]] += 1

    max_num = 0
    for a in dict_base.values():
        if max_num < a:
            max_num = a
    print('#{} {}'.format(tc, max_num))