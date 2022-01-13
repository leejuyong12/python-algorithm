import sys
sys.stdin = open('동전0.txt')

N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
cnt = 0
while K > 0:
    for x in lst:
        if K // x > 0:
            cnt += K // x
            K -= (K // x) * x
print(cnt)