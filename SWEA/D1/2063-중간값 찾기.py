N = int(input())

x = list(map(int, input().split()))
x.sort()
mid_num = (len(x) // 2)
print(x[mid_num])