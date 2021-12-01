# c 는 0~9까지 총 10개
# d 는 a~z 까지 총 26개

lst = list(input())
res = []
for x in range(len(lst)):
    if lst[x] == 'c':
        res.append(26)
    elif lst[x] == 'd':
        res.append(10)
ans = res[0]

for y in range(1, len(res)):
    if res[y] == res[y-1]:
        ans *= res[y]-1
    else:
        ans *= res[y]
print(ans)
