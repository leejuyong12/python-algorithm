import sys
sys.stdin = open('문자열 비교.txt')

TC = int(input())
for tc in range(1, TC+1):
    base = list(input())
    text = list(input())

    res = 0
    for x in range(len(text)-len(base)+1):
        cnt = 0
        for y in range(len(base)):
            if text[x+y] == base[y]:
                cnt += 1
            else:
                cnt = 0
        if cnt == len(base):
            res = 1

    print('#{} {}'.format(tc, res))