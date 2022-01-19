import sys
sys.stdin = open('한윤정이 이탈리아에 가서 아이스크림을 사먹는데.txt')

N, M = map(int, input().split())

ice = [[False] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    ice[a-1][b-1] = True
    ice[b-1][a-1] = True

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if ice[i][j] == False and ice[j][k] == False and ice[i][k] == False:
                result += 1
print(result)