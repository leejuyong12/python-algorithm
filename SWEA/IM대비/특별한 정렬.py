import sys
sys.stdin = open('특별한 정렬.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    res = []
    st = 0
    ed = len(lst)-1
    while st < ed:
        res.append(lst[ed])
        res.append(lst[st])
        ed -= 1
        st += 1
    print('#{}'.format(tc), end=' ')
    print(*res[:10])