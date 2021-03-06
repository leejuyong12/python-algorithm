import sys
sys.stdin = open('꽃길.txt')

# # dy = [0, -1, 1, 0, 0]
# # dx = [0, 0, 0, -1, 1]
# dir = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
# def check(y, x):
#     global N
#     for dy, dx in dir:
#         nx = x + dx
#         ny = y + dy
#         if 0 > ny or ny > N-1 or 0 > nx or nx > N-1 or visited[ny][nx]:
#
#             return False
#     return True
#
# def calculate(y, x):
#     global N
#     result = 0
#     for dy, dx in dir:
#         nx = x + dx
#         ny = y + dy
#         result += flowers[ny][nx]
#     return result
#
# def dfs(a, cost, cnt):
#     global answer
#     if cnt == 3:
#         answer = min(answer, cost)
#         return
#     for i in range(a, N):
#         for j in range(1, N):
#             if check(i, j):
#                 visited[i][j] = True
#                 for dy, dx in dir:
#                     visited[i+dy][j+dx] = True
#                 dfs(i, cost+calculate(i, j), cnt+1)
#                 visited[i][j] = False
#                 for dy, dx in dir:
#                     visited[i+dy][j+dx] = False
#
#
#
# N = int(input())
# flowers = [list(map(int, input().split())) for _ in range(N)]
# visited = [[False] * N for _ in range(N)]
# answer = 99999999
# dfs(1, 0, 0)
# print(answer)

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
def check(y, x):  # 범위 안에 들어있는가 - 들어있으면 True 아니면 False
    global N
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > ny or ny > N-1 or 0 > nx or nx > N-1 or visited[ny][nx]:

            return False
    return True

def calculate(y, x):  # 상하좌우가운데 합 계산
    global N
    result = 0
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        result += flowers[ny][nx]
    return result

def dfs(a, cost, cnt):
    global answer
    if cnt == 3:        # 꽃이 세개면 끝
        answer = min(answer, cost)
        return
    for i in range(a, N):
        for j in range(1, N):
            if check(i, j): # 범위 안에 들어있으면
                visited[i][j] = True # 중간에 있는거 True로 바꾸고
                for z in range(5):      # 상하좌우에 있는거 다 True로 바꾸기
                    visited[i+dy[z]][j+dx[z]] = True
                dfs(i, cost+calculate(i, j), cnt+1)  #
                visited[i][j] = False
                for z in range(5):
                    visited[i+dy[z]][j+dx[z]] = False


N = int(input())
flowers = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
answer = 99999999
dfs(1, 0, 0)
print(answer)

