import sys
sys.stdin = open('최대 상금.txt')

def sorts(base):        # base = 123
    global change
    n = len(base)       # n = 3
    for i in range(n-1):        # i = 0, 1
        maxI = i                # maxI = 0    // maxI = 1
        for j in range(i+1, n): # i = 0 j = 1, 2  // i = 1 j = 2
            if base[j] >= base[maxI]:
                maxI = j                #
        base[maxI], base[i] = base[i], base[maxI]
        change -= 1
        if change == 0:
            return base

TC = int(input())

for tc in range(1, TC+1):
    base, change = input().split()        # str(123), str(1)
    base = list(base)
    change = int(change)
    sorts(base)
    base = ''.join(base)
    print('#{} {}'.format(tc, base))





