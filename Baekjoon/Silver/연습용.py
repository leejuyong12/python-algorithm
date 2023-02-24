from collection import deque

def solution(n, computers):
    def bfs(i):
        queue = deque()
        queue.append(i)
        while queue:
            i = queue.popleft()
            visited[i] = True
            for a in range(n):
                if computers[i][a] and visited[a] == False:
                    queue.append(a)
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            bfs(i)
            answer += 1