import sys
sys.stdin = open('소수 찾기.txt')



N = int(input())
lst = list(map(int, input().split()))
cnt = 0
for x in range(N):
    check = 0
    if lst[x] > 1:
        for y in range(2, lst[x]):
            if lst[x] % y == 0:
                check += 1
        if check == 0:
            cnt += 1
print(cnt)