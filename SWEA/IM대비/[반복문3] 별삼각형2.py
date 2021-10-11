import sys
sys.stdin = open('[반복문3] 별삼각형2.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())

    if M == 1:
        a = 0
        print('#{}'.format(tc))
        for i in range(N):
            if i <= N//2:
                print('*' * (i+1))
            elif i > N//2:
                print('*' * (i-(2*a+1)))
                a += 1

    if M == 2:
        a = 0
        print('#{}'.format(tc))
        for i in range(N):
            if i <= N//2:
                print(' ' * (2-i)+ '*'* (i+1))
            elif i > N//2:
                print(' ' * (a+1)+ '*' * (i-(2*a+1)))
                a += 1

    if M == 3:
        a = 0
        new_N = N
        print('#{}'.format(tc))
        for i in range(N):
            if i <= N//2:
                print(' '* a + '*' * new_N + ' ' * a)
                if a < 2 and new_N > 1:
                    a += 1
                    new_N -= 2
                else:
                    a = 1
                    new_N = 3
            elif i > N//2:
                print(' '* a + '*' * new_N + ' ' * a)
                new_N += 2
                a -= 1
    if M == 4:
        a = 3
        print('#{}'.format(tc))
        for i in range(N):
            if i <= N//2:
                print(' ' * i + '*' * (a-i) )
            if i > N//2:
                print(' '* (a-1) + '*' * (i-1))



