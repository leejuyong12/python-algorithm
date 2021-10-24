import sys
sys.stdin = open('카나페.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    biscuit = sorted(list(map(int, input().split())), reverse=True)
    ingredient = sorted(list(map(int, input().split())), reverse=True)
    # 큰 값부터 곱해야 최종적으로 큰 값이 나온다.
    res = 0
    for x in range(N):
        res += biscuit[x] * ingredient[x]
    print('#{} {}'.format(tc, res))