N = int(input())

length = len(str(N))

cnt = 0

for i in range(length-1):
    cnt += 9 * 10 ** i * (i+1)
print(cnt + (N - 10**(length-1) + 1) * length)