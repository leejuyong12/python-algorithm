N = int(input())
lst = list(map(int, input().split()))
check = []
cnt = 0
for x in lst:
    if x not in check:
        check.append(x)
    else:
        cnt += 1
print(cnt)