import sys
sys.stdin = open('영화감독 숌.txt')

N = int(sys.stdin.readline())
start = 666
cnt = 0
while True:
    if '666' in str(start):
        cnt += 1
        if cnt == N:
            print(start)
            break
    start += 1