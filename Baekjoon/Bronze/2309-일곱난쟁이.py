import sys
sys.stdin = open('2309-일곱난쟁이-백준.txt')

K = [int(input()) for _ in range(9)]
total = sum(K)
K.sort()        # 정렬을 해줘야한다.
a = 0
b = 0
for x in range(9):
    for y in range(x+1, 9):
        if total - (K[x] + K[y]) == 100:
            a = K[x]
            b = K[y]
K.remove(a)
K.remove(b)
for i in K:
    print(i)


