import sys
sys.stdin = open('물통.txt')
from collections import deque

def check(x, y):
    if visited[x][y] == False:
        visited[x][y] = True
        queue.append((x, y))

def bfs():
    while queue:
        x, y = queue.popleft()
        # x 는 A, y 는 B, z 는 c
        z = C - x - y
        if x == 0:      # A가 비어있을때 C의 상태
            answer.append(z)

### 다시풀기
        # x -> y
        water = min(x, B-y)
        check(x - water, y + water)
        # x -> z
        water = min(x, C-z)
        check(x - water, y)
        # y -> x
        water = min(y, A-x)
        check(x + water, y - water)
        # y -> z
        water = min(y, C-z)
        check(x, y - water)
        # z -> x
        water = min(z, A-x)
        check(x + water, y)
        # z -> y
        water = min(z, B-y)
        check(x, y + water)
A, B, C = map(int, input().split())
visited = [[False] * 201 for _ in range(201)]
visited[0][0] = True
queue = deque()
queue.append((0, 0))
answer = []
bfs()
answer.sort()
for i in answer:
    print(i, end=" ")