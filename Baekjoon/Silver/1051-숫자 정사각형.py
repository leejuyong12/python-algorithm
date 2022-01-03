import sys
sys.stdin = open('숫자정사각형.txt')

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
max_num = 1
plus_length = min(N, M)
for x in range(N):
    for y in range(M):
        for num in range(plus_length+1):
            if (x + num) < N and (y + num) < M and arr[x][y] == arr[x+num][y] == arr[x][y+num] == arr[x+num][y+num]:
                compare = (num+1) * (num+1)
                if compare > max_num:
                    max_num = compare
print(max_num)