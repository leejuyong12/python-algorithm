import sys
sys.stdin = open('파스칼의삼각형.txt')

n, k = map(int, input().split())
lst = []
for x in range(1, n+1):
    lst.append([0]*x)       # 이 코드 핵심
lst[0][0] = 1
for x in range(1, n):
    for y in range(len(lst[x])):
        if y == 0 or y == x:
            lst[x][y] = 1
        else:
            lst[x][y] = lst[x-1][y-1] + lst[x-1][y]

print(lst[n-1][k-1])    # 문제읽어보면 n-1, k-1 에 유의하라고 했음