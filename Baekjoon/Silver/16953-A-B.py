import sys
sys.stdin = open('A-B.txt')

A, B = map(int, input().split())
cnt = 1
while True:
    if A == B:
        break
    elif A > B or (B % 2 != 0 and B % 10 != 1):
        cnt = -1
        break
    elif B % 2 == 0: # 짝수
        B //= 2
    elif B % 10 == 1:
        B //= 10
    cnt += 1
print(cnt)