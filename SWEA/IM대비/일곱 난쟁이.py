import sys
sys.stdin = open('일곱 난쟁이.txt')

lst = [int(input()) for _ in range(9)]

sum_lst = sum(lst)
a = 0
b = 0
lst.sort()
for x in range(len(lst)):
    for y in range(x+1, len(lst)):
        if sum_lst - lst[x] - lst[y] == 100:
            a = lst[x]
            b = lst[y]
lst.remove(a)
lst.remove(b)
for z in lst:
    print(z)