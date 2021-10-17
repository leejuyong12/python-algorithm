import sys
sys.stdin = open('영준이의 카드 카운팅.txt')

TC = int(input())
for tc in range(1, TC+1):
    cards = input()

    cnt_lst = [[0]*14 for _ in range(4)]    # S D H C 순서

    SDHC = ['S', 'D', 'H', 'C']
    result = []
    res = ''
    for i in range(len(cards)):
        if cards[i] in SDHC:
            if cards[i+1] == 0:
                cnt_lst[SDHC.index(cards[i])][int(cards[i+2])] += 1
            else:
                cnt_lst[SDHC.index(cards[i])][int(cards[i+1:i+3])] += 1
    for x in cnt_lst:
        result.append(13 - sum(x))
        for y in x:
            if y >= 2:
                res = 'ERROR'
                break
    if res != 'ERROR':
        for z in result:
            res += str((z)) + ' '
    print('#{} {}'.format(tc, res))
