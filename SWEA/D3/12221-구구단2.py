TC = int(input())

def cal(A, B):
    if A >= 10 or B >= 10:
        return -1
    else:
        return A * B

for tc in range(1, TC+1):
    A, B = map(int, input().split())

    result = cal(A, B)

    print('#{} {}'.format(tc, result))