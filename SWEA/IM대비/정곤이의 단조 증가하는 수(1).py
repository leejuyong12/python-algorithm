import sys
sys.stdin = open('정곤이의 단조 증가하는 수.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))

    res = set()
    for x in range(N):
        for y in range(x+1, N):
            num = str(lst[x] * lst[y])
            cnt = 0
            if len(num) >= 2:
                for z in range(len(num)-1):
                    if int(num[z]) <= int(num[z+1]):
                        cnt += 1
                if cnt == len(num)-1:
                    res.add(int(num))
    if len(res) > 0:
        print('#{} {}'.format(tc, max(res)))
    else:
        print('#{} {}'.format(tc, -1))



