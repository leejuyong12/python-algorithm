import sys
sys.stdin = open('생일.txt')

n = int(input())
lst = []
for _ in range(n):
    name, d, m, y = input().split()
    lst.append([name, int(d), int(m), int(y)])  # 한번에 받으면 int로 바꿔주기 어렵다.
lst.sort(key= lambda x:(x[3], x[2], x[1]))
print(lst[-1][0])
print(lst[0][0])