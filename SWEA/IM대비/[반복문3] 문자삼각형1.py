import sys

sys.stdin = open('[반복문3] 문자삼각형1.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())

    # num = 1
    # print('#{}'.format(tc))
    # for x in range(N):
    #     print(' ' * (N - x - 1) + '*' * (2 * x + 1))
    base = ''
    text = 65
    print('#{}'.format(tc))
    for x in range(1, N + 1):  # N번 반복
        for y in range(x):
            if y == 0:
                base += chr(text)
                text += 1
        if text > 90:
            text = 65

        if x < N:
            base += '\n'
    print(base)
