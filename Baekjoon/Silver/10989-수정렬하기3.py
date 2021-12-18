import sys
sys.stdin = open('수정렬하기3.txt')

N = int(sys.stdin.readline())
check = [0] * 10001

for n in range(N):
    num = int(sys.stdin.readline())
    check[num] += 1
for x in range(10001):
    if check[x] != 0:
        for y in range(check[x]):
            print(x)