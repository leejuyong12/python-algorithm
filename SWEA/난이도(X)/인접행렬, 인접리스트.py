# dfs 반복문 : 모든 vertex를 한번만 방문하여 출력
visited = [False] * 8
def dfs_f(s):
    ST = []
    ST.append(s)
    visited[s] = True

    while ST:       # len(ST) > 0:
        s = ST.pop()            # 괄호안에 안쓰면 -1
        print(s, end = ' ')
        for i in grp2[s]:
            if not visited[i]:
                ST.append(i)
                visited[i] = True

    return


# dfs 재귀 : 모든 vertex를 한번만 방문하여 출력

def dfs_r(s):
    visited[s] = True
    print(s, end=' ')
    for i in grp2[s]:
        if not visited[i]:
            dfs_r(i)
    return
# bfs 반복문 : 모든 vertext 를 한번만 방문하여 출력
def bfs(s):
    Q = []
    Q.append(s)
    visited[s] = True

    while Q:        # len(ST) > 0
        s = Q.pop(0)
        print(s, end=' ')

        for i in grp2[s]:
            if not visited[i]:
                Q.append(i)
                visited[i] = True
    return

s = '1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7'
lst = list(map(int, s.split(',')))
grp1 = [[0] * 8 for _ in range(8)]
for i in range(0, len(lst), 2):
    s1 = lst[i]
    s2 = lst[i+1]
    grp1[s1][s2] = 1
    grp1[s2][s1] = 1  # 무방향이니까 뒤집어서도 넣어줘야 한다

print(grp1)
grp2 = [[] for _ in range(8)]
for i in range(0, len(lst), 2):
    s1 = lst[i]
    s2 = lst[i+1]
    grp2[s1].append(s2)
    grp2[s2].append(s1)
print(grp2)
visited = [False] * 8

dfs_f(1)
visited = [False] * 8
print()
dfs_r(1)
print()
bfs(1)
