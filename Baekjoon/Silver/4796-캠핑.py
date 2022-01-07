import sys
sys.stdin = open('캠핑.txt')

t = 1

while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    answer = (V // P) * L + min((V % P), L)
    print('Case {}: {}'.format(t, answer))
    t += 1
