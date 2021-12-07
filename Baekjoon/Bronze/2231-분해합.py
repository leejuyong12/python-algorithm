N = int(input())
num = 0
for n in range(1, N+1):
    lst_n = list(map(int, str(n)))
    num = n + sum(lst_n)
    if num == N:
        print(n)
        break
    if n == N:
        print(0)