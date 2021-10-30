import sys
sys.stdin = open('햄버거.txt')

def comb(cnt, score, calorie):
    global result
    if calorie > L:
        return
    if score > result:
        result = score
    if cnt == N:
        return
    comb(cnt+1, score, calorie)
    comb(cnt+1, score+lst[cnt][0], calorie+lst[cnt][1])

TC = int(input())
for tc in range(1, TC+1):
    N, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    comb(0, 0, 0)
    print('#{} {}'.format(tc, result))
