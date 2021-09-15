def in_order(root):
    global answer
    if root * 2 <= N:
        in_order(root*2)
    answer += lst[root][1]
    if root * 2 + 1 <= N:
        in_order(root*2 + 1)
    return answer
TC = 10
for tc in range(1, TC+1):
    N = int(input())
    lst = [[]] + [input().split() for _ in range(N)]
    answer = ''
    print('#{} {}'.format(tc, in_order(1)))