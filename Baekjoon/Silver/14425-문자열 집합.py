import sys
sys.stdin = open('문자열집합.txt')

N, M = map(int, input().split())
S = set([input() for _ in range(N)])
check = [input() for _ in range(M)]
cnt = 0
for x in check:
    if x in S:
        cnt += 1
print(cnt)