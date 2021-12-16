N = int(input())
num = 1
start = 2
for i in range(9, N, 3):
    num += start
    start += 1
print(num)