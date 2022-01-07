import sys
sys.stdin = open('회의실배정.txt')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end_time = lst[0][1]
for x in range(1, N):
    if lst[x][0] >= end_time:
        cnt += 1
        end_time = lst[x][1]
print(lst)
print(cnt)