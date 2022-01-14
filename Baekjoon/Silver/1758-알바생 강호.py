import sys
sys.stdin = open('알바생강호.txt')

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
lst.sort(reverse=True)

ans = 0
for x in range(len(lst)):
    tip = lst[x] - ((x+1) - 1)
    if tip >= 0:
        ans += tip

print(ans)