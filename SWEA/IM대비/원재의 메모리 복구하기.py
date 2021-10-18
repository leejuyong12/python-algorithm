import sys
sys.stdin = open('원재의 메모리 복구하기.txt')

TC = int(input())
for tc in range(1, TC+1):
    base = list(input())
    lst = ['0'] * len(base)
    cnt = 0
    for x in range(len(lst)):
        if base[x] != lst[x]:
            for y in range(x+1, len(lst)):
                lst[y] = base[x]
            cnt += 1
    print(cnt)