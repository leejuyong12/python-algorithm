import sys
sys.stdin = open('2012-등수 매기기.txt')

N = int(sys.stdin.readline())
lst = []
res = 0
for _ in range(N):
    x = int(sys.stdin.readline())
    lst.append(x)
lst.sort()
# 1등하고 싶은애, 2등 하고 싶은애, ....N등 하고 싶은애
# 세서
for a in range(1, N+1):
    res += abs(lst[a-1] - a)
print(res)