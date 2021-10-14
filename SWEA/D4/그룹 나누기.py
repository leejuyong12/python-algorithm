import sys
sys.stdin = open('그룹 나누기.txt')

def find_set(x):
    if x == p[x]:
        return x

    return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    p = [i for i in range(N+1)]

    for i in range(M):
        s1 = lst[i*2]
        s2 = lst[i*2+1]
        union(s1, s2)
    # print(p)
    cnt = [0] * (N+1)
    for i in range(1, N+1):
        cnt[find_set(i)] = 1

    # print(cnt)

    print('#{} {}'.format(tc, sum(cnt)))