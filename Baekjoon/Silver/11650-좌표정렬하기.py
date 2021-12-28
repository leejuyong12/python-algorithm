import sys
sys.stdin = open('좌표정렬하기.txt')

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])
arr.sort(key=lambda x:(x, y))
for a, b in arr:
    print(a, b)