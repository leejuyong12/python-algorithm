import sys
sys.stdin = open('쥬스.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    print('#{}'.format(tc), end=' ')
    for x in range(N):
        print('{}{}{}'.format(1, '/', N), end = ' ')
    print()
