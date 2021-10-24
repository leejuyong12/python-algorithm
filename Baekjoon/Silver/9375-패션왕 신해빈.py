import sys
sys.stdin = open('패션왕.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    clothes = [input().split() for _ in range(N)]

    dict = {}
    for x in clothes:
        if x[1] not in dict:
            dict[x[1]] = 1
        else:
            dict[x[1]] += 1
    res = 1
    for y in dict.values():
        res *= (y+1)
    print(res-1)