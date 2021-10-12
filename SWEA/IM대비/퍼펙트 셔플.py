import sys
sys.stdin = open('퍼펙트 셔플.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    cards = list(input().split())

    result = ''
    if len(cards) % 2 == 0:
        for x in range(len(cards)//2):
            result += cards[x] + ' '
            result += cards[x+len(cards)//2] + ' '

    if len(cards) % 2 == 1:
        for x in range(len(cards)//2+1):
            result += cards[x] + ' '
            if x + len(cards)//2 +1 < len(cards):
                result += cards[x+len(cards)//2+1] + ' '

    print('#{} {}'.format(tc, result))