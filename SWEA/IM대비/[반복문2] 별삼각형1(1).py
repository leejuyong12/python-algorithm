import sys
sys.stdin = open('[반복문2] 별삼각형1.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())

    base = ''
    if M == 1:
        print('#{}'.format(tc))
        for x in range(N):
            print('*' * (x+1))
    if M == 2:
        print('#{}'.format(tc))
        for x in range(N):
            print('*' * (N-x))
    if M == 3:
        num = 1
        print('#{}'.format(tc))
        for x in range(N):
            print(' '* (N-x-1) + '*'*(2*x+1))
