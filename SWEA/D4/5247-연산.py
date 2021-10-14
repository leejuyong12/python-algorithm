import sys
sys.stdin = open('연산.txt')
from collections import deque

def solve():
    Q = deque()
    Q.append((N, 0))
    while Q:
        curV, cnt = Q.popleft()

        if curV == M:
            return cnt

        t = [curV+1, curV-1, curV*2, curV-10]
        for newV in t:
            if 0 < newV <= 1000000 and not visited[newV]:
                visited[newV] = True
                Q.append((newV, cnt+1))


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    visited = [False] * 1000001
    print('#{} {}'.format(tc, solve()))
