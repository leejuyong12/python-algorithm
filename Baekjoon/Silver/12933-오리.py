import sys
sys.stdin = open('오리.txt')

listen = input()
duck = ['q', 'u', 'a', 'c', 'k']
visited = [0] * len(duck)

check = 0
ans = 0
for x in range(len(listen)):
    if listen[x] == duck[check]:
        visited[check] += 1
        check += 1
        if visited[check] == 1:
            visited[check] = 0


        if check == len(duck) - 1:
            check = 0

        if 0 not in visited:
            ans += 1
            visited = [0] * len(duck)
if ans == 0:
    print(-1)
else:
    print(ans)

# 정답
# duck = input()
# visited = [False] * len(duck)
# cnt = 0
#
# if len(duck) % 5 != 0:
#     print(-1)
#     exit()
#
#
# def solve(start):
#     global cnt
#     quack = 'quack'
#     j = 0
#     first = True
#     for i in range(start, len(duck)):
#         if duck[i] == quack[j] and not visited[i]:
#             visited[i] = True
#             if duck[i] == 'k':
#                 if first:
#                     cnt += 1
#                     first = False
#                 j = 0
#                 continue
#             j += 1
#
#
# for i in range(len(duck)):
#     if duck[i] == 'q' and not visited[i]:
#         solve(i)
#
# if not all(visited) or cnt == 0:
#     print(-1)
# else:
#     print(cnt)
