import sys
sys.stdin = open('[반복문3] 별삼각형2.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())

    if M == 1:
        print('#{}'.format(tc))
        for i in range(N):
            if i <= N//2:
                print('*' * (i+1))
            elif i > N//2:
                print('*' * (N-i))

    if M == 2:
        print('#{}'.format(tc))
        for i in range(N):
            if i <= N//2:
                print(' '* (N//2-i) + '*'*(i+1))
            else:
                print(' '* (i-N//2) + '*'*(N-i))

    if M == 3:
        print('#{}'.format(tc))
        for i in range(N):
            if i <= N//2:
                print(' '* i + '*'*(N-i*2) + ' '*i)
            else:
                print(' '*(N-i-1) + '*'*(N-(N-i-1)*2) + ' '*(N-i-1))
    if M == 4:
        print('#{}'.format(tc))
        for i in range(N):
            if i <= N//2:
                print(' '*i + '*'*(N//2+1-i))
            else:
                print(' '*(N//2) + '*' * (i-1) + ' '* (N-i-1))



