N = int(input())
result = 1
if N == 0:
    print(1)
else:
    for x in range(2, N+1):
        result *= x
    print(result)