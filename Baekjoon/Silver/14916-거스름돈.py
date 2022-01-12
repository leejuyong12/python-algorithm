import sys
sys.stdin = open('거스름돈.txt')

N = int(input())

# 2원과 5원이 있다.
cnt = 0
while N > 0:
    if N % 5 == 0:
        print(N // 5 + cnt)
        break
    N -= 2
    cnt += 1

if N < 0:
    print(-1)

