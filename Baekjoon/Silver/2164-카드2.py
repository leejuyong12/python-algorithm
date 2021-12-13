import sys
sys.stdin = open('카드2.txt')
from collections import deque


# N = int(input())
N = int(sys.stdin.readline())

queue = deque()
for n in range(1, N+1):
    queue.append(n)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
for x in range(len(queue)):
    print(queue[x])

# 시간 줄이기
# N = int(input())
# square = 2
# while True:
#     if (N == 1 or N == 2):
#         print(N)
#         break
#     square *= 2
#     if (square >= N):
#         print(N - (square // 2) * 2)
#         break
