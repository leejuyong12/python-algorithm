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